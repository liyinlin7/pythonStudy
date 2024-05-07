<template>
    <div>
        <BreadCrumb></BreadCrumb>
       测试计划详情页
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'
import BreadCrumb from '@/components/common/BreadCrumb.vue'

export default {
    components: {
        BreadCrumb
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

</style>