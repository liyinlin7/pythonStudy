<template>
    <el-form ref="form" :model="form" label-width="80px">
        <el-row :gutter="20">
            <el-col :span="12">
            <el-form-item label="题目id">
                <el-input v-model="form.question_id" style="width:100%;"></el-input>
            </el-form-item>
            </el-col>
            <el-col :span="12">
            <el-form-item label="题目归属">
                <el-select v-model="form.type" placeholder="请选择归属区域" style="width:100%;">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="12">
            <el-form-item label="题目类型">
                <el-checkbox-group v-model="form.question_type">
                <el-checkbox label="选择题" name="type"></el-checkbox>
                <el-checkbox label="判断题" name="type"></el-checkbox>
                <el-checkbox label="其他" name="type"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            </el-col>
            <el-col :span="12">
            <el-form-item label="范围">
                <el-checkbox-group v-model="form.range">
                <el-checkbox label="区域" name="type"></el-checkbox>
                <el-checkbox label="全国" name="type"></el-checkbox>
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
import { reactive, toRefs } from 'vue'
import { useRoute } from 'vue-router'  // 导入路由， 不是useRouter路由器

export default {
    components: {
    },
    setup () {
        const state = reactive({
            form: {
                question_id: '',
                type: [],
                question_type: [],
                range: [],
            }
        })
        // 1.总数据条数
        const total = inject("total")
        // 2. 每页显示多少条
        const pageSize = inject('pageSize')
        // 3.第几页
        const currentPage = ref(1)
        // 5.每页显示条数下拉的改变
        const getData = inject("getData")
        // const route = useRoute()   // 获取当前路由
        // state.routeList = route.matched   // 获取当前路由的数组
        // console.log('route', route)
        // console.log('state.routeList', state.routeList)
        function onSubmit(){

        }
        function clear(){
            state.form = {
                question_id: '',
                type: [],
                question_type: [],
                range: [],
            }
        }
        return {
                ...toRefs(state),
            }
        }
    }
</script>

<style scoped>

</style>