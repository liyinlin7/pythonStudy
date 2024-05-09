<template>
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
import { reactive, toRefs, inject, ref } from 'vue'

export default {
    setup () {
        const formCopy = inject('formCopy')
        const state = reactive({
            form: formCopy.value
        })
        // console.log('formRef', formRef.value)
        // const state = reactive({
        //     form: formRef.value
        // })
        // 1.总数据条数
        const total = inject("total")
        // 2. 每页显示多少条
        const pageSize = inject('pageSize')
        // 3.第几页
        const currentPage = ref(1)
        // 5.每页显示条数下拉的改变
        const getData = inject("getData")
        const handleSizeChange = (size) => {
            // pageSize.value = size
            currentPage.value = 1
            getData(pageSize.value, currentPage.value)
        }
        // 6.当前页码的改变，触发方法
        const handleCurrentChange = (index) => {
            // currentPage.value = index
            console.log(state.form)
            const formData = JSON.stringify(state.form)
            getData(pageSize.value, index, formData)
        }
        return {
            ...toRefs(state),
            handleSizeChange,
            handleCurrentChange,
            total,
            pageSize,
            getData,
            currentPage,
        }
    }
}
</script>

<style lang="scss" scoped>
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