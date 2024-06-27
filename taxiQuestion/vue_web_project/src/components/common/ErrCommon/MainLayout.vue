<template>
    <div>
        <el-row>
            <el-col :span="24"><div class="grid-content ep-bg-purple-dark" />
                <!-- 面包屑组件 -->
                <BreadCrumb></BreadCrumb>
            </el-col>
        </el-row>
         <el-row>
            <el-col :span="24"><div class="grid-content ep-bg-purple-dark" />
                <!-- 搜索栏 -->
                <SearchBar></SearchBar>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24"><div class="grid-content ep-bg-purple-dark" />
                <!--表格组件 -->
                <Tables></Tables>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24">
                <!--分页组件 -->
                <Paginator></Paginator>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'
import BreadCrumb from '@/components/common/ErrCommon/BreadCrumb.vue'
import SearchBar from '@/components/common/ErrCommon/SearchBar.vue'
import Tables from '@/components/common/ErrCommon/Tables.vue'
import Paginator from '@/components/common/ErrCommon/Paginator.vue'

export default {
    components: {
        BreadCrumb, Tables, Paginator, SearchBar
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

.el-row {
  margin-bottom: 20px;
  text-align: center;

}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>