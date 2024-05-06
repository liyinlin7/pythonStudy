<template>
    <div ref= 'bg' class='bg'>
        <!-- 背景第三方插件
            安装命令：npm install canvas-nest.js
         -->
    </div>
</template>

<script>
import { ref, onMounted, getCurrentInstance, onBeforeUnmount } from 'vue'
import CanvasNest from "canvas-nest.js"

export default {
    setup () {
        const bg = ref()
        onMounted(() => {
            getCurrentInstance().cn = new CanvasNest(bg.value, config)
        })
        // 离开页面的时候销毁 背景插件
        onBeforeUnmount(() => {
            getCurrentInstance().cn.destroy()
        })
        //color的值为RGB的取值
        // opacity是鼠标与各个点之间连线的透明值
        // zIndex是特效显示的优先层级
        // count是背景中漂浮点的数量
        const config = {
            // color: "255, 255, 255",
            color: "18, 156, 255",
            opacity: 1,
            zIndex: 5,
            count: 50,
        }
        return {
            bg
        }
    }
}
</script>

<style lang="scss" scoped>
.bg{
    width: 95vw;
    height: 95vh;
}
</style>