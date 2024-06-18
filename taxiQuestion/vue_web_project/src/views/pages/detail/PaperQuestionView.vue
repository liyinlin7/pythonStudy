<template>
  <el-row>
    <el-col :span="24">
      <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
          题目区域
        </el-col>
      </el-row>
    </el-col>
    <el-col :span="24">
      <el-row :gutter="24" align= 'center'>
        <el-col :span="24">
          选项区域
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import BreadCrumb from '@/components/common/BreadCrumb.vue'
import { inject } from 'vue'
import { reactive } from "@vue/reactivity"
import { useRoute } from 'vue-router'
export default {
  components: {
    BreadCrumb,
  },
  setup() {
    const totle = inject('inject')
    return {
      reactive,
      totle,
      useRoute
    }
  },
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.title {
  text-align: left;
  width: 120px;
}
.newLine{
  float:right;
}
</style>