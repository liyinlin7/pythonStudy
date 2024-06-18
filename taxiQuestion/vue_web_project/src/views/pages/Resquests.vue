<template>
    <!--  $route.path  获取当前路由地址 -->
    <div v-if="$route.path === '/resquests'">
        <MainLayout></MainLayout>
    </div>
    <router-view v-else></router-view>
</template>

<script>
// 跨组件传参，引入 provide
import { reactive, toRefs, onMounted, ref, provide  } from 'vue'
import MainLayout from '@/components/common/ResquestCommon/MainLayout.vue'
import { getResquest } from '@/utils/api.js'
import moment from 'moment'

export default {
    components: {
        MainLayout
    },
    setup () {
        const state = reactive({
            count: 0,
            form: {
                paperId: '',
                paperName: '',
                paperType: [],
                paperRange: [],
                paperQuestionType: [],
                createTime: ''
            },
        })
        // 1.定义标题/字段对象数组
        const columns = [
            {
                title: '试卷ID',          //列的标题
                field: 'paperId',      //数据的字段名
            },
            {
                title: '考试名称',          //列的标题
                field: 'paperName',      //数据的字段名
            }, {
                title: '题目分类',
                field: 'paperType',
                formatter: (row, column, cellValue, index) => {
                    if (cellValue !== null) {
                        const arrayData = cellValue.replace(/'/g, '"')
                        let listItems = []
                        listItems = JSON.parse(arrayData)
                        let str = ''
                        for (let i = 0; i < listItems.length; i++) {
                            str += listItems[i] + ','
                        }
                        return str.substring(0, str.length - 1)
                    } else {
                        return cellValue !== null ?  cellValue : '全部'
                    }
                }
            }, {
                title: '范围',
                field: 'paperRange',
                formatter: (row, column, cellValue, index) => {
                    return cellValue === 1 ? '区域' : (cellValue === 2 ? '全国' : '全部')
                }
            }, {
                title: '题目类型',
                field: 'paperQuestionType',
                formatter: (row, column, cellValue, index) => {
                    if (cellValue !== null && cellValue.length > 1) {
                        let str = ''
                        for (let i = 0; i < cellValue.length; i++) {
                            if (cellValue[i] === '1') {
                                str += '选择题,'
                            } else if (cellValue[i] === '2') {
                                str += '判断题,'
                            } else if (cellValue[i] === '3') {
                                str += '服务五句话,'
                            }
                        }
                        return str.substring(0, str.length - 1)
                    } else {
                        return cellValue === '1' ? '选择题' : cellValue === '2' ? '判断题' : cellValue === '3' ? '服务五句话' : cellValue === null ? '全部' : '未知类型'
                    }
                }
            }, {
                title: '创建时间',
                field: 'createTime',
                formatter: (row, column, cellValue, index) => {
                    let jsDate = convertDateTimeStringToFormat(cellValue)
                    return jsDate
                }
            }
        ]
        const convertDateTimeStringToFormat = (dateTimeString) => {
            const momentObj = moment(dateTimeString.replace(' GMT', ''), 'DD MMM YYYY HH:mm:ss')
            // 验证是否成功解析
            if (momentObj.isValid()) {
                // 使用format方法将日期时间对象转换为指定格式的字符串
                const formattedDateTime = momentObj.format('YYYY-MM-DD HH:mm:ss')
                return formattedDateTime
            } else {
                // 处理解析失败的情况
                return 'Invalid date time string'
            }
        }
        const formCopy = ref(state.form)
        // 2.待显示的数据
        const tableData = ref([]) // 定义一个响应式数据
        const total = ref(0) // 定义一个响应式数据
        const getData = (pageSize, pageIndex, form) => {
                currentPage.value = pageIndex
                getResquest(`/paper_opt/paperSelect?page_size=${pageSize}&pageIndex=${pageIndex}&arges=${form}`) // 使用 ` 反引号 然后 ${形参} 引用
                // getResquest('/requests/', { page_size: pageSize, page_index: pageIndex })
                .then(
                    (res) => {
                        // console.log("res", res.data.data)
                        // 2.1 列表数据
                        tableData.value = res.data.data
                        // tableData.value = res.data.retlist
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
        const currentPage = ref(1)
        onMounted(() => {
            getData(pageSize.value, currentPage.value, formCopy.value)
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
        provide('currentPage', currentPage)
        return {
            ...toRefs(state),
            columns,
        }
    }
}
</script>

<style lang="scss" scoped>

</style>