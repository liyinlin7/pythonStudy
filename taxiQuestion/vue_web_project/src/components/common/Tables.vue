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
        <el-button size="small" type="danger" @click="updateCollect(scope.$index, scope.row)">{{ scope.row.collect === 1 ? '收藏' : '取消收藏' }} </el-button>
      </template>
    </el-table-column>
  </el-table>
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
            currentPage: currentPageCopy
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
          router.push(`${route.path}/` + row.question_id)
        }
        const getData = inject("getData")
        const pageSize = inject('pageSize')
        const updateCollect = (index, row) => {
          // // console.log('删除方法被调用：', index, row)
          let dataValue = {
            question_id: row.question_id,
            collect: null
          }
          if (row.collect === 1) {
            dataValue.collect = 0
          } else if (row.collect === 0) {
            dataValue.collect = 1
          }
          let headers = {
            'Content-Type': 'application/json'
          }
          postResquest(`/questions_opt/updateCollect`, dataValue, headers)
          .then((res) => {
              ElMessage.success(res.data.message)
              const formData = JSON.stringify(state.form)
              getData(pageSize.value, state.currentPage, formData)
            }
          )
          .catch((err) => {
              ElMessage.err(err.data.message)
          })
        }
        return {
            ...toRefs(state),
            tableData,
            columns,
            handleEdit,
            updateCollect
        }
    }
}
</script>

<style lang="scss" scoped>

</style>