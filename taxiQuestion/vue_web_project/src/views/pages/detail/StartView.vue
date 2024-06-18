<template>
  <el-row justify="center">
    <el-col :span="24">
      <BreadCrumb></BreadCrumb>
    </el-col>
  </el-row>
  <el-col :span="24">
      <PaperQuesion></PaperQuesion>
  </el-col>
  <el-col :span="24" align= 'center'>
      <el-button type="primary" @click="back">上一题</el-button>
      <el-button @click="commit">提交答案</el-button>
      <el-button type="primary" @click="next">下一题</el-button>
  </el-col>
  <el-col :span="24">
    <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
        </el-col>
      </el-row>
      <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
          <div v-for="row in tableData.value" :key="row.key"   :value="row.index+1">{{index+1}}</div>
        </el-col>
      </el-row>
  </el-col>

</template>

<script>
import BreadCrumb from '@/components/common/ResquestCommon/BreadCrumb.vue'
import PaperQuesion from '@/views/pages/detail/PaperQuestionView.vue'
import { reactive } from "@vue/reactivity"
import { inject, ref, onMounted, provide } from 'vue'
import { useRoute } from 'vue-router'
import { getResquest } from '@/utils/api.js'
import { ElMessageBox, ElMessage } from 'element-plus'
// import { caseDetail } from '@/httplib'
export default {
  components: {
    BreadCrumb, ElMessageBox, ElMessage, PaperQuesion
  },
  setup() {
    const questionBool = ref()
    const state = reactive({
      count: 0,
    })
    // 1.总数据条数
    const total = ref()
    // 2. 每页显示多少条
    const tableData = ref([])
    const route = useRoute()
    // 获取动态路由别名ID的值
    const paperId = route.params.paperId
    const getData = () => {
            getResquest(`/paper_opt/selectPaperQuestion?paperId=${paperId}&questionBool=${questionBool.value}`) // 使用 ` 反引号 然后 ${形参} 引用
            .then(
                (res) => {
                    // 2.1 列表数据
                    // console.log('res.data.data', res.data.data)
                    // tableData.value = res.data.data
                    // console.log('tableData.value', tableData.value)
                    tableData.value = res.data.retlist
                    total.value = res.data.total
                }
            )
        }
    onMounted(() => {
        getData()
      })
    const back = () => {
        }
    const commit = () => {
        }
    const next = () => {
        }
    provide('total', total)
    return {
      state,
      getData,
      inject,
      paperId,
      total,
      back,
      commit,
      next
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