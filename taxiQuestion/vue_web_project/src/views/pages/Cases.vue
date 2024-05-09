<template>
    <!--  $route.path  获取当前路由地址 -->
    <div v-if="$route.path === '/questions'">
        <MainLayout></MainLayout>
    </div>
    <router-view v-else></router-view>
</template>

<script>
// 跨组件传参，引入 provide
import { reactive, toRefs, onMounted, ref, provide } from 'vue'
import MainLayout from '@/components/common/MainLayout.vue'
import { getResquest } from '@/utils/api.js'

export default {
    components: {
        MainLayout
    },
    setup () {
        const state = reactive({
            count: 0,
            form: {
                question_id: '',
                question_type: [],
                range: [],
                type_op: '',
                collect: []
            },
        })
        // 1.定义标题/字段对象数组
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
                    return cellValue === 1 ? '选择题' : (cellValue == 2 ? '判断题' : '服务五句话')
                }
            }, {
                title: '范围',
                field: 'range',
                formatter: (row, column, cellValue, index) => {
                    return cellValue === 1 ? '区域' : '全国'
                }
                // icon: 'el-icon-time',  //图标信息-非必填
            }, {
                title: '是否收藏',
                field: 'collect',
                formatter: (row, column, cellValue, index) => {
                    return cellValue === 1 ? '没收藏' : '收藏'
                }
                // icon: 'el-icon-time',  //图标信息-非必填
            }
        ]
        const formCopy = ref(state.form)
        // formCopy.value = state.form
        // console.log('2222222222211111', formCopy.value.question_id)
        // 2.待显示的数据
        const tableData = ref([]) // 定义一个响应式数据
        const total = ref(0) // 定义一个响应式数据
        const getData = (pageSize, pageIndex, form) => {
                getResquest(`/questions?page_size=${pageSize}&pageIndex=${pageIndex}&arges=${form}`) // 使用 ` 反引号 然后 ${形参} 引用
                .then(
                    (res) => {
                        // 2.1 列表数据
                        tableData.value = res.data.data
                        // 2.2 总数据条数
                        total.value = res.data.total
                    }
                )
            }
        const typeData = ref([])
        const getType = () => {
            getResquest(`/questions_opt/questionType`)
            .then(
                (res) => {
                    typeData.value = res.data.data
                }
            )
        }
        // 3. 当页面挂载完毕，自动从后台获取数据
        const pageSize = ref(10)
        onMounted(() => {
            console.log('加载')
            getData(pageSize.value, 1, formCopy.value)
            getType()
        })
        // 4.对子、孙组件提供数据，语法类似 set(key, value)   value 可以是变量，也可以是一个函数方法
        provide('tableData', tableData) // 4.1 展示的列表数据
        provide('columns', columns)  // 4.2 列的标题（表头）
        provide('getData', getData)  // 4.3 分页接口方法
        provide('total', total)  // 4.4 总数据条数
        provide('pageSize', pageSize)  // 4.5 每页显示条数
        provide('typeData', typeData)
        provide('formCopy', formCopy)
        return {
            ...toRefs(state),
            columns,
        }
    }
}
</script>

<style lang="scss" scoped>

</style>