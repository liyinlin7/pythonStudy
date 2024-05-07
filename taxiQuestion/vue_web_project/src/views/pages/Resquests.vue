<template>
    <div>
        <MainLayout></MainLayout>
    </div>
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
        })
        // 1.定义标题/字段对象数组
        const columns = [
            {
                title: '请求方法',          //列的标题
                field: 'method',      //数据的字段名
            }, {
                title: '请求url',
                field: 'url',
            }, {
                title: '请求头',
                field: 'headers',
            }, {
                title: '请求参数',
                field: 'parmas',
            }
        ]
        // 2.待显示的数据
        const tableData = ref([]) // 定义一个响应式数据
        const total = ref(0) // 定义一个响应式数据
        const getData = (pageSize, pageIndex) => {
                getResquest(`/requests/?page_size=${pageSize}&page_index=${pageIndex}`) // 使用 ` 反引号 然后 ${形参} 引用
                // getResquest('/requests/', { page_size: pageSize, page_index: pageIndex })
                .then(
                    (res) => {
                        // 2.1 列表数据
                        tableData.value = res.data.retlist
                        // 2.2 总数据条数
                        total.value = res.data.total
                    }
                )
            }
        // 3. 当页面挂载完毕，自动从后台获取数据
        const pageSize = ref(10)
        onMounted(() => {
            getData(pageSize.value, 1)
        })
        // 4.对子、孙组件提供数据，语法类似 set(key, value)   value 可以是变量，也可以是一个函数方法
        provide('tableData', tableData) // 4.1 展示的列表数据
        provide('columns', columns)  // 4.2 列的标题（表头）
        provide('getData', getData)  // 4.3 分页接口方法
        provide('total', total)  // 4.4 总数据条数
        provide('pageSize', pageSize)  // 4.5 每页显示条数
        return {
            ...toRefs(state),
            columns,
        }
    }
}
</script>

<style lang="scss" scoped>

</style>