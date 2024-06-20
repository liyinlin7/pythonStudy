<template>
  <el-row justify="center">
    <el-col :span="24">
      <BreadCrumb></BreadCrumb>
    </el-col>
  </el-row>
  <el-row>
  <el-col :span="24">
      <div v-if="form_.question_id !== ''">
      <PaperQuesion></PaperQuesion>
      </div>
  </el-col>
  </el-row>
  <el-row>
  <el-col :span="24" align= 'center'>
      <el-button type="primary" @click="back">上一题</el-button>
      <el-button @click="commit">提交答案</el-button>
      <el-button type="primary" @click="next">下一题</el-button>
  </el-col>
  </el-row>
  <el-row>
  <el-col :span="24">
    <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
        </el-col>
      </el-row>
      <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
          <el-col :span="24">题目总数：{{paperQuestionDatatotal}}</el-col>
        </el-col>
      </el-row>
  </el-col>
  </el-row>
  <el-row align= 'center'>
    <el-col :span="9"></el-col>
    <el-col :span="6">
      <div class="grid-container">
        <el-button circle v-for="number_ in numbers" :key="number_" @click="onButtonClick(number_)"
        :class="['ellipse-button', 'circle', { 'light-blue-background': number === number_ },
        { 'answer-background': isNaN(paperQuestionData[ number_ -1 ].user_answer) }]">
        {{ number_ }}
        </el-button>
      </div>
    </el-col>
    <el-col :span="2"></el-col>
  </el-row>
</template>

<script>
import BreadCrumb from '@/components/common/ResquestCommon/BreadCrumb.vue'
import PaperQuesion from '@/views/pages/detail/PaperQuestionView.vue'
import { ref, onMounted, provide, reactive, toRefs } from 'vue'
import { useRoute } from 'vue-router'
import { getResquest, postResquest } from '@/utils/api.js'
import { ElMessageBox, ElMessage } from 'element-plus'
// import { caseDetail } from '@/httplib'
export default {
  components: {
    BreadCrumb, ElMessageBox, ElMessage, PaperQuesion
  },
  setup() {
    // const questionBool = ref()
    const state = reactive({
      count: 0,
      form_: {
        question_id: ''
        },
      paperQuestionData: [],
      paperQuestionDatatotal: 0,
      numbers: null,
      number: 1,
      questionAnswer: '',
      questionBool: ''
    })
    const formQ = ref(state.form_)
    const questionData = ref([])
    const option = ref('')
    const route = useRoute()
    // 获取动态路由别名ID的值
    const paperId = route.params.paperId
    const getPaperQuestion = () => {
      getResquest(`/paper_opt/selectPaperQuestion?paperId=${paperId}`) // 使用 ` 反引号 然后 ${形参} 引用
      .then(
          (res) => {
              // 2.1 列表数据
              // console.log('res.data.data', res.data.data)
              state.paperQuestionData = res.data.data
              state.paperQuestionDatatotal = res.data.total
              // console.log('state.form.paperQuestionData', state.paperQuestionData)
              let questionId = res.data.data[0].question_id
              getData(questionId)
              state.numbers = generateNumbers()
          }
      )
    }
    const getData = (questionId) => {
      // console.log("请求接口：questionId", questionId)
      state.form_.question_id = questionId
      const formData = JSON.stringify(state.form_)
      getResquest(`/questions?page_size=10&pageIndex=1&arges=${formData}`) // 使用 ` 反引号 然后 ${形参} 引用
      .then(
          (res) => {
              // 2.1 列表数据
              questionData.value = res.data.data
              // console.log('res.data.data:', res.data.data)
              // if (res.data.data.length != 0) {
                // state.questionAnswer =  res.data.data[-1].question_answer
                // console.log('state.questionAnswer:', state.questionAnswer)
              // }
          }
      )
      }
    const generateNumbers = () => {
      return Array.from({ length: state.paperQuestionDatatotal }, (_, index) => index + 1)
    }
    const onButtonClick = (number) => {
      state.number = number
      let questionIdIndex = number - 1
      let questionId = state.paperQuestionData[questionIdIndex].question_id
      getData(questionId)
    }
    onMounted(() => {
        getPaperQuestion()
    })
    const back = () => {
      let num = state.number -= 1
      // console.log('你点击了数字:', state.number)
      if (num <= 0) {
        ElMessage({
          message: '已经是第一题了',
          type: 'success',
        })
        state.number = 1
      } else {
        let questionIdIndex = state.number - 1
        let questionId = state.paperQuestionData[questionIdIndex].question_id
        getData(questionId)
      }
    }
    const commit = () => {
      // console.log(option.value)
      state.questionAnswer = state.paperQuestionData[state.number - 1].question_answer
      if (state.questionAnswer === '对') {
        state.questionAnswer = '正确'
      } else if (state.questionAnswer === '错') {
        state.questionAnswer = '错误'
      }
      if (state.questionAnswer === option.value) {
        state.questionBool = 'True'
      }  else if (state.questionAnswer !== option.value) {
        state.questionBool = 'False'
      }
      let dataValue = {
            paperId: paperId,
            questionBool: state.questionBool,
            questionId: state.paperQuestionData[state.number - 1].question_id,
            userAnswer: option.value
          }
      let headers = {
        'Content-Type': 'application/json'
      }
      postResquest(`/paper_opt/updatePaperQuestion`, dataValue, headers)
          .then((res) => {
              ElMessage.success(res.data.message)
              state.paperQuestionData[state.number -  1].user_answer = option.value
              next()
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
    const next = () => {
      let num = state.number += 1
      if (num > state.paperQuestionDatatotal) {
        ElMessage({
          message: '已经是最后一题了',
          type: 'success',
        })
        state.number = state.paperQuestionDatatotal
      } else {
        let questionIdIndex = state.number
        // console.log('next', questionIdIndex)
        let questionId = state.paperQuestionData[questionIdIndex - 1].question_id
        getData(questionId)
      }
        }
    provide('questionData', questionData)
    provide('formQ', formQ)
    provide('option', option)
    return {
      ...toRefs(state),
      paperId,
      back,
      commit,
      next,
      onButtonClick,
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
.flex-container {
  display: flex;
  flex-wrap: wrap; /* 允许换行 */
  justify-content: center; /* 可选，居中对齐容器 */
}

.circle-button {
  /* 假设每个按钮和间隙共占1/13的空间，可以根据实际情况调整 */
  width: calc((100% / 12) - 5px); /* 减去左右间隙 */
  margin-left: 5px;
}
.circle + .circle {
  margin-left: 5px; /* 或使用其他单位和值 */
  margin-block: 5px;
}
.light-blue-background {
  background-color: lightblue; /* 设置为你想要的浅蓝色 */
  border: 1px solid #3399FF;
}
.answer-background {
  background-color: rgb(207, 247, 222); /* 设置为你想要的浅蓝色 */
}
</style>