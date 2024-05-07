<template>
  <!-- <nav> -->
    <!-- 声明式导航方式
    路由链接：自动渲染为a标签，href的值为to的值
      to属性，值可以是字符串，也可以是对象
      query属性{ id: 123, name: '张三'}，在路由后面添加参数  ？id=123&name=张三
    -->
  <!--
    <router-link to="/">Home</router-link> |
    <router-link :to="{path:'/'}">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link :to="{name: 'about', query: { id: 123, name: '张三'}}">About</router-link>
  -->
  <!-- </nav> -->

  <router-view/>  <!-- 路由插槽 -->
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
