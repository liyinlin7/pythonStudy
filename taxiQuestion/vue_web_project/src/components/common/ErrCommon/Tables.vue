<template>
  <el-table :data="tableData" style="width: 100%">
    <!-- prop的值要与参数名对应 -->
    <!-- <el-table-column prop="date" label="Date" width="180" />
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="address" label="Address" /> -->
    <el-table-column :prop="itemObj.field" :label="itemObj.title" v-for="(itemObj, index) in columns" :key="index" :formatter="itemObj.formatter" />
    <el-table-column label="操作">
      <template #default="scope">
        <!-- <el-button size="small" @click="handleEdit(scope.$index, scope.row)">修改</el-button> -->
        <!-- <el-button size="small" type="primary" @click="start(scope.$index, scope.row)">题目详情</el-button> -->
        <el-button type="primary" @click="open(scope.$index, scope.row)">题目详情</el-button>
        <!-- <el-button size="small" type="danger" @click="deletePager(scope.$index, scope.row)">删除</el-button> -->
      </template>
    </el-table-column>
  </el-table>
  <el-dialog
      v-model="centerDialogVisible"
      title="题目详情"
      width="30%"
      center>
      <div>问：{{titleBefor}}</div>
      <div style="margin-top: 10px;">{{titleAfterA}}</div>
      <div style="margin-top: 5px;">{{titleAfterB}}</div>
      <div style="margin-top: 5px;">{{titleAfterC}}</div>
      <div style="margin-top: 5px;">{{titleAfterD}}</div>
      <div style="color:red; margin-top: 10px;">正确答案：{{questionAnswer}}</div>
      <div></div>
      <div class="dialog-footer" style="text-align: center; margin-top: 20px;">
        <el-button type="primary" @click="centerDialogVisible = false">确 定</el-button>
      </div>
  </el-dialog>
</template>

<script>
// 跨组件传参，接收父或祖父传递的参数，导入 inject
import { reactive, toRefs, inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { postResquest } from '@/utils/api.js'
import { ElMessage } from 'element-plus'

// 1、列表数据的传入: a.父传子 b.插槽  【c.跨组件传值】
// 2、 label显示的标题：定义一个变量【对象数组】
// 3、for 循环来显示列数，对步骤2的变量进行循环
export default {
    setup () {
        const currentPageCopy = inject("currentPage")
        const formCopy = inject('formCopy')
        const state = reactive({
            form: formCopy.value,
            currentPage: currentPageCopy,
            centerDialogVisible: false,
            title: '',
            questionAnswer: '',
            titleBefor: '',
            titleAfterA: '',
            titleAfterB: '',
            titleAfterC: '',
            titleAfterD: ''
        })
        // 3.接收上层组件提供的数据，语法格式相当于 ：get(key) 或 get(ket, [默认值]),
        // inject  inject(key) , inject(key,[默认值]) 如果key没值，就会使用用默认值
        const tableData = inject('tableData')
        const columns = inject('columns')
        const router = useRouter()
        const route = useRoute()
        const handleEdit = (index, row) => {
          // console.log('tableData', tableData)
          // console.log('修改方法被调用：', index, row)
          // router.push(`${route.path}/` + row.question_id)
          router.push(`${route.path}/` + 'addView')
        }
        const getData = inject("getData")
        const pageSize = inject('pageSize')
        const deletePager = (index, row) => {
          // console.log('修改方法被调用：', index, row)
          let dataValue = {
            paperId: row.paperId
          }
          let headers = {
            'Content-Type': 'application/json'
          }
          // console.log('dataValue', dataValue)
          postResquest(`/paper_opt/deletePaper`, dataValue, headers)
          .then((res) => {
              ElMessage.success(res.data.message)
              const formData = JSON.stringify(state.form)
              getData(pageSize.value, state.currentPage, formData)
            }
          )
          .catch((err) => {
            try {
              ElMessage.err(err.data.message)
            } catch (error) {
              ElMessage.err(error)
            }
          })
        }
        const start = (index, row) => {
            let paperId = row.paperId
            router.push(`${route.path}/` + 'startView/' + `${paperId}`)
        }
        const open =  (index, row) => {
          console.log('row', row)
          state.title = row.question_title
          state.titleAfterA = ''
          state.titleAfterB = ''
          state.titleAfterC = ''
          state.titleAfterD = ''
          const targetCharA = 'A'
          const targetCharB = 'B'
          const targetCharC = 'C'
          const targetCharD = 'D'
          const charIndexA = state.title.indexOf(targetCharA)
          const charIndexB = state.title.indexOf(targetCharB)
          const charIndexC = state.title.indexOf(targetCharC)
          const charIndexD = state.title.indexOf(targetCharD)
          // console.log('charIndex', charIndex)
          // 截取到特定字符前的内容
          if (charIndexA !== -1) {
            state.titleBefor = state.title.substring(0, charIndexA)
            // 截取特定字符后的所有内容
            state.titleAfterA = state.title.substring(charIndexA - 1, charIndexB)
            state.titleAfterB = state.title.substring(charIndexB - 1, charIndexC)
            state.titleAfterC = state.title.substring(charIndexC - 1, charIndexD)
            state.titleAfterD = state.title.substring(charIndexD)
          } else {
            state.titleBefor = state.title
          }
          state.questionAnswer = row.question_answer
          state.centerDialogVisible = true
        }
        return {
            ...toRefs(state),
            tableData,
            columns,
            handleEdit,
            deletePager,
            start,
            open,
        }
    }
}
</script>

<style lang="scss" scoped>

</style>