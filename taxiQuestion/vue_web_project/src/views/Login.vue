<template>
    <BackGround></BackGround>
    <div class="title">测试</div>
    <div class='login-form'>
        <el-form v-bind:model="loginForm" :rules="rules" ref="ruleFormRef" label-width="120px">
            <div class='text-header'>用户登录</div>
            <el-form-item label="用户名：" prop="user_phone">
                <el-input v-model="loginForm.user_phone" />
            </el-form-item>
            <el-form-item label="密码："  prop="password">
                <el-input show-password v-model="loginForm.password" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit(ruleFormRef)">登录</el-button>
                <el-button type='info' @click="clear(ruleFormRef)">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import { reactive, ref } from 'vue'
import  BackGround from '@/components/BackGround.vue'  //@指向的是  src文件夹
import { postResquest } from '@/utils/api.js'   // 导入自己封装的axios
import { ElMessage } from 'element-plus'  //  导入使用 element的消息提示插件
import { useRouter } from 'vue-router'   // 导入路由器

export default {
    components: {
        BackGround
    },
    setup () {
        const loginForm = reactive({
            user_phone: '',
            password: '',
        })
        const ruleFormRef = ref()
        const rules = reactive({
            user_phone: [
                { required: true, message: '请输入用户名', trigger: 'blur' }
            ],
            password: [
                { required: true, message: '请输入密码', trigger: 'blur' },
                { min: 5, max: 12, message: '请输入6-12位字符', trigger: 'blur' },
            ]
        })
        const router = useRouter()   // 创建一个新的路由器对象
        const onSubmit = async (ruleFormRef) => {
            if (!ruleFormRef) return
            await ruleFormRef.validate((valid, fields) => {
                if (valid) {
                    console.log('submit!')
                    postResquest('/login', loginForm)  // 引用导入封装的axios方法
                    .then((response) => {  // 接口成功之后执行方法
                        console.log(response)
                        const token = response.data.token
                        // localStorage.setItem('isLogin', 'yes')  //  localStorage  跟cookies 差不多，本地存储数据，关闭浏览器也会继续存在,不安全
                        sessionStorage.setItem('token', token)  //  sessionStorage  跟cookies 差不多，本地存储数据，关闭浏览器就会清除
                        ElMessage.success(response.data.msg)   // 消息类型：success、warning、info、error
                        router.push('/about')
                    })
                    .catch((error) => {  //  接口失败之后执行方法
                        console.log(error)
                    })
                } else {
                    // console.log('error submit!', fields)
                }
            })
        }
        const clear = (ruleFormRef) => {
            if (!ruleFormRef) return
            ruleFormRef.resetFields()
        }

        return {
            loginForm,
            onSubmit,
            clear,
            rules,
            ruleFormRef
        }
    }
}
</script>

<style lang="scss" scoped> // scoped 定义的css属性 只作用当前页面
.text-header{
    text-align: center;
    font-size: 20px;
    color: rgb(16, 16, 16);
    margin-bottom: 30px;
}
.login-form {
  position: absolute;
  width: 400px;
  height: 400px;
  top: 200px;
  right: 300px;
  border-radius: 10px;
  box-shadow: 1px 1px 5px #333;
  display: flex;
  justify-content: center;
  align-items: center;
}
.title{
    position: absolute;
    width: 400px;
    height: 80px;
    top: 50px;
    right: 300px;
    display: flex;
    justify-content: center;
    align-content: center;
    font-size: 60px;
    font-family: 'Microsoft Yahei';
    color: rgb(13, 104, 139);
}
.el-form-item{
    color: black;
    margin-right: 50px;
    width:300px;
}

</style>