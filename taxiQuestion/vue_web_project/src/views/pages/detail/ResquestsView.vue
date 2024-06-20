<template>
  <el-row justify="center">
    <el-col :span="24">
      <BreadCrumb></BreadCrumb>
    </el-col>
  </el-row>
  <el-form ref="form" :model="form" label-width="80px">
    <!-- <el-form ref="formRef" :model="form" label-width="80px"> -->
        <el-row :gutter="24">
            <el-col :span="6">
            <el-form-item label="题目类型">
                <el-checkbox-group v-model="state.form.paperQuestionType">
                <el-checkbox label="选择题" name="question_type" value="1"></el-checkbox>
                <el-checkbox label="判断题" name="question_type" value="2"></el-checkbox>
                <el-checkbox label="其他" name="question_type" value="3"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
            <el-col :span="8">
            <el-form-item label="范围">
                <el-checkbox-group v-model="state.form.paperRange">
                <el-checkbox label="区域" name="range" value="1"></el-checkbox>
                <el-checkbox label="全国" name="range" value="2"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
        </el-row>
        <el-row :gutter="24">
            <el-col :span="8">
            <el-form-item label="题目归属">
                <el-select v-model="state.form.paperType" multiple  placeholder="请选择归属区域" style="width:100%;">
                <el-option v-for="item in typeData" :key="item.key"  :label="item" :value="item"></el-option>
                <!-- <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option> -->
                </el-select>
            </el-form-item>
            </el-col>
            <!-- <el-col :span="8">
              <el-form-item label="试卷名称">
                  <el-input v-model="state.form.paperName" style="width:100%;"></el-input>
              </el-form-item>
            </el-col> -->
        </el-row>
        <el-form-item>
            <el-button type="primary" @click="search">搜索</el-button>
            <el-button @click="clear">重置</el-button>
             <!-- 触发模态框的按钮 -->
            <el-button type="primary" @click="open">创建</el-button>
        </el-form-item>
        <el-table :data="tableData" style="width: 100%">
          <el-table-column :prop="itemObj.field" :label="itemObj.title" v-for="(itemObj, index) in columns" :key="index" :formatter="itemObj.formatter" />
        </el-table>
    </el-form>
    <!-- 模态框组件 -->
    <nav style="text-align: center">
        <el-pagination
        v-model:currentPage="currentPage"
        v-model:page-size="pageSize"
        :page-sizes="[10, 20, 30, 50]"
        background
        layout="total, sizes, prev, pager, next"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        />
        <!--
            layout：分页组件显示哪些内容 => prev 前一页，pager 页数，next 后一页  控制页面显示的顺序
            background 背景样式
            total 总数据条数
            v-model:page-size 每页显示多条数
            v-model:currentPage  当前第几页
            @size-change 方法是结合 v-model:page-size 使用
        -->
    </nav>
</template>

<script>
import BreadCrumb from '@/components/common/ResquestCommon/BreadCrumb.vue'
import { reactive } from "@vue/reactivity"
import { inject, ref } from 'vue'
import { useRouter } from 'vue-router'
import { getResquest, postResquest } from '@/utils/api.js'
import { ElMessageBox, ElMessage } from 'element-plus'
// import { caseDetail } from '@/httplib'
export default {
  components: {
    BreadCrumb, ElMessageBox, ElMessage
  },
  setup() {
    const columns = [
            {
                title: '题目id',          //列的标题
                field: 'question_id',      //数据的字段名
            }, {
                title: '题目内容',
                field: 'question_title',
            }, {
                title: '答案',
                field: 'question_answer',
            }, {
                title: '题目归属',
                field: 'type',
            }, {
                title: '题目类型',
                field: 'question_type',
                formatter: (row, column, cellValue, index) => {
                    return cellValue === 1 ? '选择题' : cellValue === 2 ? '判断题' : cellValue === 3 ? '服务五句话' :  cellValue === null ? '全部' : '未知类型'
                }
            }, {
                title: '范围',
                field: 'range',
                formatter: (row, column, cellValue, index) => {
                    return cellValue === 1 ? '区域' : (cellValue === 2 ? '全国' : '全部')
                }
                // icon: 'el-icon-time',  //图标信息-非必填
            }, {
                title: '是否收藏',
                field: 'collect',
                formatter: (row, column, cellValue, index) => {
                    return cellValue === 1 ? '未收藏' : '已收藏'
                }
                // icon: 'el-icon-time',  //图标信息-非必填
            }
        ]
    const state = reactive({
      count: 0,
      showModal: false, // 控制模态框的显示与隐藏
      form: {
          paperId: '',
          paperName: '',
          paperType: [],
          paperRange: [],
          paperQuestionType: [],
          createTime: '',
          type_op: []
      },
    })
    const getData = (pageSize, pageIndex, form) => {
        let form_ = {
            range: state.form.paperRange,
            type_op: state.form.paperType,
            question_type: state.form.paperQuestionType
        }
        const formData = JSON.stringify(form_)
        currentPage.value = pageIndex
        // pageSize.value = pageSize
        getResquest(`/questions?page_size=${pageSize}&pageIndex=${pageIndex}&arges=${formData}`) // 使用 ` 反引号 然后 ${形参} 引用
        .then(
            (res) => {
                // 2.1 列表数据
                tableData.value = res.data.data
                // 2.2 总数据条数
                total.value = res.data.total
            }
        )
    }
    const typeData = inject('typeData')
    function open() {
      ElMessageBox.prompt('请输入创建考卷名称 ', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputPattern: /^[\u4e00-\u9fa5a-zA-Z0-9]{1,20}$/,
          inputErrorMessage: '必填长度20（汉子、英文、数字）'
      }).then(({ value }) => {
            state.form.paperName = value
            onSubmit()
      }).catch(() => {
          ElMessage({
            type: 'info',
            message: '取消输入'
        })
      })
    }
    function search() {
      state.form.type_op = state.form.paperType
      const formData = JSON.stringify(state.form)
      getData(pageSize.value, currentPage.value, formData)
    }
    function onSubmit() {
      let headers = {
            'Content-Type': 'application/json'
          }
      // const formData = JSON.stringify(state.form)
      // console.log('typeof formData', typeof formData)
      postResquest(`/paper_opt/paperInstall`, state.form, headers)
      router.push('/resquests')
    }
    function clear() {
      console.log('clear')
    }
    const router = useRouter()
    // 获取动态路由别名ID的值
    // 1.总数据条数
    const total = ref(0)
    // 2. 每页显示多少条
    const pageSize = ref(10)
    // 3.第几页
    const currentPage = ref(1)
    const tableData = ref([])
    // const getData = (pageSize, pageIndex, form) => {
    //             currentPage.value = pageIndex
    //             getResquest(`/questions?page_size=${pageSize}&pageIndex=${pageIndex}&arges=${form}`) // 使用 ` 反引号 然后 ${形参} 引用
    //             // getResquest('/requests/', { page_size: pageSize, page_index: pageIndex })
    //             .then(
    //                 (res) => {
    //                     // console.log("res", res.data.data)
    //                     // 2.1 列表数据
    //                     // console.log('res.data.data', res.data.data)
    //                     tableData.value = res.data.data
    //                     // console.log('tableData', tableData.value)
    //                     // tableData.value = res.data.retlist
    //                     // 2.2 总数据条数
    //                     total.value = res.data.total
    //                 }
    //             )
    //         }
    const handleSizeChange = (size) => {
        pageSize.value = size
        const formData = JSON.stringify(state.form)
        getData(size, currentPage.value, formData)
    }
    // 6.当前页码的改变，触发方法
    const handleCurrentChange = (index) => {
        currentPage.value = index
        // console.log(state.form)
        const formData = JSON.stringify(state.form)
        getData(pageSize.value, index, formData)
    }

    return {
      state,
      onSubmit,
      clear,
      typeData,
      search,
      handleSizeChange,
      handleCurrentChange,
      total,
      tableData,
      columns,
      open
    }
  },
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.title {
  text-align: left;
  width: 120px;
}
.newLine{
  float:right;
}
.demo-pagination-block + .demo-pagination-block {
  margin-top: 10px;
}
.demo-pagination-block .demonstration {
  margin-bottom: 16px;
}
.el-pagination{
    width: 500px;
    margin-left: 35%;
}
</style>