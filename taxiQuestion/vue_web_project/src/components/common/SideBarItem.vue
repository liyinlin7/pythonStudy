<template>
    <div>
        <el-menu-item :index="itemObj.path" v-for="(itemObj, index) in routeList" :key="index">
          <!-- icon 因为是组件标签，所以要用SVG的图片格式 -->
          <!-- <el-icon v-html="itemObj.meta.icon "></el-icon> -->
          <el-icon v-html="itemObj.meta.icon "></el-icon>
          <template #title>{{itemObj.meta.cName}}</template>
        </el-menu-item>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'

export default {
    props: { routeList: Array },
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

</style>