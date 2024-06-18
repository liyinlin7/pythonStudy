import { createApp } from 'vue'
import App from './App.vue'   // 路由介绍
import ElementPlus from 'element-plus'  // 全局导入element plus
import 'element-plus/dist/index.css'
import router from './router'
import store from './store'
import zhCn  from 'element-plus/es/locale/lang/zh-cn'   // 导入中文语言包
/*
    参数配置配置
    size：表单默认组件尺寸大小  small(小的)/mini(最小)/medium(中等)
    zIndex: 弹框尺寸大小， 默认是2000
*/
const app = createApp(App)
app.use(store).use(router).use(ElementPlus,  { locale: zhCn }).mount('#app')
