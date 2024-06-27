<template>
    <el-form ref="formCopy" :model="form" label-width="80px">
    <!-- <el-form ref="formRef" :model="form" label-width="80px"> -->
        <el-row :gutter="20">
            <el-col :span="8">
            <el-form-item label="试卷id">
                <el-input v-model="form.paperId" style="width:100%;"></el-input>
            </el-form-item>
            </el-col>
            <el-col :span="8">
            <el-form-item label="试卷名称">
                <el-input v-model="form.paperName" style="width:100%;"></el-input>
            </el-form-item>
            </el-col>
            <el-col :span="8">
            <el-form-item label="题目归属">
                <el-select v-model="form.paperType" multiple  placeholder="请选择归属区域" style="width:100%;">
                <el-option v-for="item in typeData" :key="item.key"  :label="item" :value="item"></el-option>
                <!-- <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option> -->
                </el-select>
            </el-form-item>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="10">
            <el-form-item label="题目类型">
                <el-checkbox-group v-model="form.paperQuestionType">
                <el-checkbox label="选择题" name="question_type" value="1"></el-checkbox>
                <el-checkbox label="判断题" name="question_type" value="2"></el-checkbox>
                <el-checkbox label="其他" name="question_type" value="3"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
            <el-col :span="8">
            <el-form-item label="范围">
                <el-checkbox-group v-model="form.paperRange">
                <el-checkbox label="区域" name="range" value="1"></el-checkbox>
                <el-checkbox label="全国" name="range" value="2"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
            <el-col :span="6">
            <el-form-item label="是否收藏">
                <el-checkbox-group v-model="form.collect">
                <el-checkbox label="已收藏" name="collect" value="0"></el-checkbox>
                <el-checkbox label="未收藏" name="collect" value="1"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
        </el-row>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">搜索</el-button>
            <el-button @click="clear">重置</el-button>
            <!-- <el-button type="primary" @click="createPaper()">新建试卷</el-button> -->
        </el-form-item>
    </el-form>
</template>

<script>
import { reactive, toRefs, inject } from 'vue'
// import { useRouter, useRoute } from 'vue-router'
// import { useRoute } from 'vue-router'  // 导入路由， 不是useRouter路由器

export default {
    components: {
    },
    setup () {
        const formCopy = inject('formCopy')
        const state = reactive({
            form: formCopy.value
        })
        // 1.总数据条数
        const total = inject("total")
        // 2. 每页显示多少条
        const pageSize = inject('pageSize')
        // 3.第几页
        const currentPage = inject('currentPage')
        // 5.每页显示条数下拉的改变
        const getData = inject("getData")
        // const route = useRoute()   // 获取当前路由
        // state.routeList = route.matched   // 获取当前路由的数组
        // console.log('route', route)
        // console.log('state.routeList', state.routeList)
        const onSubmit = () => {
            const formData = JSON.stringify(state.form)
            // console.log('formCopy:',  formCopy.value)
            getData(pageSize.value, currentPage.value, formData)
            }
        const typeData = inject('typeData')
        const clear = () => {
            // state.form.questionId = ''
            // console.log(state.form)
            state.form = {
                form: {
                    question_id: '',
                    question_type: [],
                    range: [],
                    type_op: '',
                    collect: []
            },
                }
            const formData = JSON.stringify(state.form)
            // console.log('formCopy:',  formCopy.value)
            getData(pageSize.value, currentPage.value, formData)
            }
        // const router = useRouter()
        // const route = useRoute()
        // const createPaper = () => {
        //     router.push(`${route.path}/` + 'addView')
        //     }
        return {
                ...toRefs(state),
                total,
                pageSize,
                currentPage,
                getData,
                onSubmit,
                clear,
                typeData,
                // createPaper
            }
        }
    }
</script>

<style scoped>

</style>