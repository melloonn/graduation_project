import { createApp } from "vue";
import App from "./App.vue";
// import TheLoginVue from "./components/TheLogin.vue";
// import TheSignUpVue from "./components/TheSignUp.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
// import { createRouter, createWebHistory } from "vue-router";
import router from "./router/router";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faPhone } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import vue3GoogleLogin from "vue3-google-login";

library.add(faPhone);
const app = createApp(App);

app.config.productionTip = false;
app.config.globalProperties.$axios = axios;
app.config.globalProperties.$isDarkMode = false;

app.component("font-awesome-icon", FontAwesomeIcon);
app.use(vue3GoogleLogin, {
  clientId:
    "285929938114-ied8ghrn6cmkvqedsi28d1vlepnbb5or.apps.googleusercontent.com",
});
app.use(ElementPlus);
app.use(router);

app.mount("#app");

axios.interceptors.response.use(
  (response) => {
    console.log("用到攔截器!"); // Log message when the interceptor is used
    return response;
  },
  async (error) => {
    if (error.response.status === 401) {
      try {
        // 嘗試自動更新 access token
        const refreshToken = sessionStorage.getItem("refresh");
        if (refreshToken) {
          const { data } = await axios.post(
            "http://127.0.0.1:8000/login/refresh/",
            {
              refresh: refreshToken,
            }
          );
          sessionStorage.setItem("access", data.access);

          // 重新發送原始請求
          error.config.headers["Authorization"] = `Bearer ${data.access}`;
          return axios(error.config);
        } else {
          throw new Error("No refresh token available");
        }
      } catch (err) {
        // 如果 refresh 失敗，強制登出並重導向到登入頁
        sessionStorage.removeItem("access");
        sessionStorage.removeItem("refresh");
        router.push("/home");
        return Promise.reject(error);
      }
    }
    return Promise.reject(error);
  }
);
