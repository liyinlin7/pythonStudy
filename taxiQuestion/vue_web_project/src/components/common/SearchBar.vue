<template>
    <el-form ref="formCopy" :model="form" label-width="80px">
    <!-- <el-form ref="formRef" :model="form" label-width="80px"> -->
        <el-row :gutter="20">
            <el-col :span="12">
            <el-form-item label="题目id">
                <el-input v-model="form.question_id" style="width:100%;"></el-input>
            </el-form-item>
            </el-col>
            <el-col :span="12">
            <el-form-item label="题目归属">
                <el-select v-model="form.type_op" placeholder="请选择归属区域" style="width:100%;">
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
                <el-checkbox-group v-model="form.question_type">
                <el-checkbox label="选择题" name="question_type" value="1"></el-checkbox>
                <el-checkbox label="判断题" name="question_type" value="2"></el-checkbox>
                <el-checkbox label="其他" name="question_type" value="3"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
            <el-col :span="8">
            <el-form-item label="范围">
                <el-checkbox-group v-model="form.range">
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
        </el-form-item>
    </el-form>
</template>

<script>
import { reactive, toRefs, inject } from 'vue'
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
        const currentPage = pageSize.value
        // 5.每页显示条数下拉的改变
        const getData = inject("getData")
        // const route = useRoute()   // 获取当前路由
        // state.routeList = route.matched   // 获取当前路由的数组
        // console.log('route', route)
        // console.log('state.routeList', state.routeList)
        const onSubmit = (pageSize, index) => {
            // console.log('question_id:', state.form.question_id, typeof state.form.question_id)
            // console.log('question_type:', state.form.question_type, typeof state.form.question_type)
            // console.log('range:', state.form.range, typeof state.form.range)
            // console.log('type:', state.form.type, typeof state.form.type)
            // console.log('collect:', state.form.collect, typeof state.form.collect)
            const formData = JSON.stringify(state.form)
            // console.log('formCopy:',  formCopy.value)
            getData(pageSize.value, index, formData)
            }
        const typeData = inject('typeData')
        const clear = (pageSize, index) => {
            // state.form.questionId = ''
            console.log(state.form)
            state.form = {
                    question_id: '',
                    question_type: [],
                    range: [],
                    type: '',
                    collect: []
                }
            const formData = JSON.stringify(state.form)
            // console.log('formCopy:',  formCopy.value)
            getData(pageSize.value, index, formData)
            }
        return {
                ...toRefs(state),
                total,
                pageSize,
                currentPage,
                getData,
                onSubmit,
                clear,
                typeData,
            }
        }
    }
</script>

<style scoped>

</style>