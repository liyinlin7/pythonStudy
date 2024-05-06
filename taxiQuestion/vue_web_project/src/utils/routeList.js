// 遍历选择自己对应了路由
export const routerList = (routeList, name) => {
    for (let i = 0; i < routeList.length; i++) {
        if (routeList[i].name === name) {
            return routeList[i]
        }
      }
}