// 針對葉面切換的router功能

import { createRouter, createWebHistory } from "vue-router";

// import TheLogin from "../components/TheLogin.vue";
// import TheRegister from "../components/TheRegister.vue";
import TheHome from "../components/TheHome.vue";
import TheMain from "../components/TheMain.vue";
import TheProfile from "@/components/TheProfile.vue";
import TheEnterpriseSelection from "../components/TheEnterpriseSelection.vue";
import TheIndicators from "../components/TheIndicators.vue";
import TheIdeas from "../components/TheIdeas.vue";
import TheCategory from "../components/TheCategory.vue";

const routes = [
  {
    // path: "/", // 路径
    // name: "Home",
    // redirect: "/login", // 重定向
  },
  {
    // path: "/login", // 路径
    // name: "Login",
    // component: TheLogin, // 跳转到的组件
  },
  {
    // path: "/register", // 路径
    // name: "Register",
    // component: TheRegister, // 跳转到的组件
  },
  {
    path: "/home",
    name: "Home",
    component: TheHome,
  },
  {
    path: "/profile",
    name: "Profile",
    component: TheProfile,
  },
  {
    path: "/main",
    name: "Main",
    component: TheMain,
  },
  {
    path: "/enterprise_selection",
    name: "Enterprise Select",
    component: TheEnterpriseSelection,
  },
  {
    path: "/indicators",
    name: "Indicators",
    component: TheIndicators,
  },
  {
    path: "/category",
    name: "Category",
    component: TheCategory,
  },
  {
    path: "/ideas",
    name: "Ideas",
    component: TheIdeas,
  },
  {
    path: "/unity",
    beforeEnter() {
      // 讓伺服器處理這個路徑，而不是 Vue Router
      window.location.href = "/unity/index.html";
    },
  },
  // {
  //   path: "/game",
  //   name: "Game",
  //   component: TheGameVue,
  // }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

// router.beforeEach((to, from, next) => {
//   let isAuthenticated = !!sessionStorage.getItem("userInfo");
//   // 如果路由要跳转到除了登录和注册的界面的话就判断是否已经登录，如果没有登录就强制跳到登录界面
//   if (to.path !== "/login" && to.path !== "/register" && !isAuthenticated) {
//     next({ path: "/login" });
//     Message({
//       message: "Please login first！",
//       type: "warning",
//     });
//   } else next();
// });

export default router;
