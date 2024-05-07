<template>
  <div class="common-layout">
    <el-container>
      <el-header>
         <slot name='header'></slot>
      </el-header>
      <el-container>
        <el-aside width="200px">
            <slot name='aside'></slot>
        </el-aside>
        <el-main>
            <slot name='main'></slot>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import { reactive, toRefs } from 'vue'

export default {

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
.common-layout{
    font-family: '微软雅黑';
    text-align: center;
}

.el-header{
    background-color: var(--el-table-header-bg-color);
    color: var(--el-text-color-primary);
    --el-header-padding: 0, 0px;
    line-height: 60px;
}
.el-aside{
    background-color: var(--el-table-header-bg-color);
    color: var(--el-text-color-primary);
}
.el-main{
    background-color: var(--el-table-header-bg-color);
    color: var(--el-text-color-primary);
}
</style>