<template>
    <div>
        <el-breadcrumb separator=">">
            <el-breadcrumb-item :to="item.path" v-for="(item, index) in routeList" :key="index">{{ item.meta.cName }}</el-breadcrumb-item>
        </el-breadcrumb>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'
import { useRoute } from 'vue-router'  // 导入路由， 不是useRouter路由器

export default {
    setup () {
        const state = reactive({
            routeList: Array
        })
        const route = useRoute()   // 获取当前路由
        state.routeList = route.matched   // 获取当前路由的数组
        // console.log('route', route)
        // console.log('state.routeList', state.routeList)
        return {
            ...toRefs(state),
        }
    }
}
</script>

<style lang="scss" scoped>

</style>