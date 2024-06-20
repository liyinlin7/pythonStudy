<template>
  <el-row>
    <el-col :span="24">
       <el-button type="primary" round @click="start">开始做题</el-button>
    </el-col>
  </el-row>
  <el-row>
    <el-col :span="24">
      <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
          <h2 align= 'left'>题目区域：</h2>
          <!-- {{dataTitle}} -->
          <h3 align= 'left'>问：{{titleBefor}}</h3>
          <h3 align= 'left'>{{titleAfter}}</h3>
          <h4 v-if="isNaN(userAnswer)">
            <div v-if="questionBool === 'True'"><i style="color: red;">回答正确</i></div>
            <div v-if="questionBool === 'False'"><i style="color: red;">回答错误</i></div>
            <div>正确答案：<i style="color: red;">{{questionAnswer}}</i></div>
          </h4>
        </el-col>
      </el-row>
    </el-col>
    <el-col :span="24">
      <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
          <h3 align= 'left'>选项区域：</h3>
          <div v-if="question_type === 1">
            <el-radio v-model="option_" label="A" border>A</el-radio>
            <el-radio v-model="option_" label="B" border>B</el-radio>
            <el-radio v-model="option_" label="C" border>C</el-radio>
            <el-radio v-model="option_" label="D" border>D</el-radio>
          </div>
          <div v-if="question_type === 2">
            <el-radio v-model="option_" label="正确" border>正确</el-radio>
            <el-radio v-model="option_" label="错误" border>错误</el-radio>
          </div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import BreadCrumb from '@/components/common/BreadCrumb.vue'
import { inject, toRefs, reactive, watchEffect } from 'vue'
import { useRoute } from 'vue-router'
import { getResquest } from '@/utils/api.js'
export default {
  components: {
    BreadCrumb,
  },
  setup() {
    const tableData_ = inject('questionData')
    const paperQuestionData_ = inject('paperQuestionData')
    const option_ = inject('option')
    const number_ = inject('number')
    const formQ = inject('formQ')
    const state = reactive({
      tableData: tableData_,
      dataTitle: '',
      titleBefor: '',
      titleAfter: '',
      count: 0,
      form: formQ.value,
      paperQuestionData: paperQuestionData_,
      paperQuestionDatatotal: 0,
      option: '',
      dataList: null,
      question_type: 0,
      userAnswer: '',
      questionBool: null,
      paperId: '',
      questionAnswer: '',
    })
    // const data = () => {
    //   // console.log("typeof tableData", typeof state.tableData)
    //   state.dataList = tableData_.value
    // }
    const start = () => {
        // console.log('state.form.question_id', state.form.question_id)
        // console.log('dataTitle', state.tableData[0].question_title)
        state.dataTitle = state.tableData[0].question_title
        state.question_type = state.tableData[0].question_type
    }
    const seletPaperQuestion = () => {
      getResquest(`/paper_opt/selectPaperQuestion?paperId=${state.paperId}&questionId=${state.form.question_id}`)
      .then(
          (res) => {
              // 2.1 列表数据
              // console.log('res.data.data', res.data.data)
              state.userAnswer = res.data.data[0].user_answer
              state.questionBool = res.data.data[0].question_bool
              state.questionAnswer = res.data.data[0].question_answer
              // console.log('userAnswer', state.userAnswer)
          }
      )
    }
    const route = useRoute()
    state.paperId = route.params.paperId
    watchEffect(() => {
      // 这个函数会在tableData变化时重新执行
      if (state.tableData[0] !== undefined) {
        state.dataTitle = state.tableData[0].question_title
        state.question_type = state.tableData[0].question_type
        state.option = ''
        // console.log('question_id', state.form.question_id)
        seletPaperQuestion()
        if (isNaN(state.userAnswer)) {
          state.option = state.userAnswer
        }
        const targetChar = 'A'
        const charIndex = state.dataTitle.indexOf(targetChar)
        // 截取到特定字符前的内容
        state.titleBefor = state.dataTitle.substring(0, charIndex)
        // 截取特定字符后的所有内容
        state.titleAfter = state.dataTitle.substring(charIndex)
        option_.value = state.option
      }
    })
    return {
      ...toRefs(state),
      tableData_,
      start,
      paperQuestionData_,
      number_,
      option_
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
</style>