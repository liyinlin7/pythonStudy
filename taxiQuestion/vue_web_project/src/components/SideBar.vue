<template>
    <div style="height:100%;">
        <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical"
        default-active="2"
        text-color="#fff"
        :router='true'
        :collapse='isCollapse'
        > <!-- menu里的router 是否启动menu-item是否启动路由，当启动的时候 index作为path进行路由跳转 -->
        <SideBarItem :routeList='routesList'></SideBarItem>
        <el-menu-item @click="collapseButton" index=''>
          <el-icon v-if="isCollapse == false"><ArrowLeftBold /></el-icon>
          <el-icon v-else><ArrowRightBold /></el-icon>
        </el-menu-item>
      </el-menu>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'
// import { Document,  Menu as IconMenu,  Location,  Setting, ArrowLeftBold, ArrowRightBold } from '@element-plus/icons-vue'
import {  ArrowLeftBold, ArrowRightBold } from '@element-plus/icons-vue'
import SideBarItem from './common/SideBarItem.vue'  // 侧边栏升级---> 导入工具栏子组件SideBarItem
import { useRouter } from 'vue-router'
import { routerList } from '@/utils/routeList.js'

export default {
    components: {
        // Document, IconMenu,  Location,  Setting, ArrowLeftBold, ArrowRightBold,
        ArrowLeftBold, ArrowRightBold, SideBarItem,
    },
    setup () {
        const state = reactive({
            count: 0,
            isCollapse: false,
            routesList: [],
        })
        const collapseButton = () => {
            state.isCollapse = !state.isCollapse
            let el = document.getElementsByClassName('el-aside')
            if (state.isCollapse === false) {
                el[0].setAttribute("style", "width: 200px")
            } else {
              setTimeout(() => {
                el[0].setAttribute("style", "width: 70px")
              }, 185)
            }
        }
        // // 侧边栏升级---> 获取路由器
        const router = useRouter()
        const routerLst = router.options.routes
        state.routesList = routerList(routerLst, 'home').children  // 调用自己封装的方法，获取自己想要的路由
        // 遍历所有路由列表  找到自己想要的，防止路由接口调整之后，获取不到
        // for (let i = 0; i < routerLst.length; i++) {
        //   if (routerLst[i].name === 'home1') {
        //     state.routesList = routerLst[i].children
        //   }
        // }
        return {
            ...toRefs(state),
            collapseButton,
        }
    }
}
</script>

<style lang="scss" scoped>
.el-menu-vertical{
  height: 100%;
}
</style>