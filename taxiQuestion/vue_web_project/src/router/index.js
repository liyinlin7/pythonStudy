// import { NULL } from 'sass'
import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/Home.vue'),
    children: [
      {
        path: '/questions',
        name: 'questions',
        meta: { // meta 添加自定义属性
          icon: '<svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa=""><path fill="currentColor" d="M280.768 753.728 691.456 167.04a32 32 0 1 1 52.416 36.672L314.24 817.472a32 32 0 0 1-45.44 7.296l-230.4-172.8a32 32 0 0 1 38.4-51.2l203.968 152.96zM736 448a32 32 0 1 1 0-64h192a32 32 0 1 1 0 64H736zM608 640a32 32 0 0 1 0-64h319.936a32 32 0 1 1 0 64H608zM480 832a32 32 0 1 1 0-64h447.936a32 32 0 1 1 0 64H480z"></path></svg>',
          cName: '题库',
        },
        component: () => import('../views/pages/Cases.vue'),
        children: [
          {
            path: ':id',  //动态路由， :+别名
            meta: {
              cName: '题目',
            },
            component: () => import('../views/pages/detail/CasesView.vue')
          }
        ]
      },
      {
        path: '/resquests',
        name: 'resquests',
        meta: {
          icon: '<svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa=""><path fill="currentColor" d="M389.44 768a96.064 96.064 0 0 1 181.12 0H896v64H570.56a96.064 96.064 0 0 1-181.12 0H128v-64h261.44zm192-288a96.064 96.064 0 0 1 181.12 0H896v64H762.56a96.064 96.064 0 0 1-181.12 0H128v-64h453.44zm-320-288a96.064 96.064 0 0 1 181.12 0H896v64H442.56a96.064 96.064 0 0 1-181.12 0H128v-64h133.44z"></path></svg>',
          cName: '考试管理',
        },
        component: () => import('../views/pages/Resquests.vue'),
        children: [
          {
            path: 'addView',
            meta: {
              cName: '考试新增',
            },
            component: () => import('../views/pages/detail/ResquestsView.vue')
          },
          {
            path: 'startView/:paperId',
            meta: {
              cName: '试卷答题',
            },
            component: () => import('../views/pages/detail/StartView.vue')
          }
        ]
      },
      {
        path: '/plans',
        name: 'plans',
        meta: {
          icon: '<svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa=""><path d="m199.04 672.64 193.984 112 224-387.968-193.92-112-224 388.032zm-23.872 60.16 32.896 148.288 144.896-45.696L175.168 732.8zM455.04 229.248l193.92 112 56.704-98.112-193.984-112-56.64 98.112zM104.32 708.8l384-665.024 304.768 175.936L409.152 884.8h.064l-248.448 78.336L104.32 708.8zm384 254.272v-64h448v64h-448z" fill="currentColor"></path></svg>',
          cName: '试卷练习',
        },
        component: () => import('../views/pages/Plans.vue'),
        children: [
          {
            path: ':id',  //动态路由， :+别名
            meta: {
              cName: '测试计划详情',
            },
            component: () => import('../views/pages/detail/PlansView.vue')
          }
        ]
      },
      {
        path: '/reports',
        name: 'reports',
        meta: {
          icon: '<svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa=""><path fill="currentColor" d="M128 224v512a64 64 0 0 0 64 64h640a64 64 0 0 0 64-64V224H128zm0-64h768a64 64 0 0 1 64 64v512a128 128 0 0 1-128 128H192A128 128 0 0 1 64 736V224a64 64 0 0 1 64-64z"></path><path fill="currentColor" d="M904 224 656.512 506.88a192 192 0 0 1-289.024 0L120 224h784zm-698.944 0 210.56 240.704a128 128 0 0 0 192.704 0L818.944 224H205.056z"></path></svg>',
          cName: '错题库',
        },
        component: () => import('../views/pages/Reports.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === '/') {
    next()
  } else if (sessionStorage.getItem('token') !== '' && sessionStorage.getItem('token') !== null) {
    // console.log(sessionStorage.getItem('token'))
    next()
  } else {
    // next(false)
    next('/')
  }
})

export default router
