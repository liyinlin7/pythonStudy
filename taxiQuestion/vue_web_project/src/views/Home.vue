<template>
    <div>
        <Layout>
            <!-- 具名插槽 -->
            <template #header><NavBar></NavBar></template>
            <template #aside><SideBar></SideBar></template>
            <template #main>
                <!--   路由占位符 -->
                <router-view></router-view>
            </template>
        </Layout>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'

import Layout from '@/components/Layout.vue'
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'

export default {
    components: {
        Layout,
        NavBar,
        SideBar
    },
    setup () {
        const state = reactive({
            count: 0,
        })

        return {
            ...toRefs(state),

        }
    }
}
</script>

<style lang="scss" scoped>
.aside{
    height: 100%;
}
</style>