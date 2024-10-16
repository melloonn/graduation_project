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

library.add(faPhone);
const app = createApp(App);

app.config.productionTip = false;
app.config.globalProperties.$axios = axios;
app.config.globalProperties.$isDarkMode = false;

app.component("font-awesome-icon", FontAwesomeIcon);

app.use(ElementPlus);
app.use(router);

app.mount("#app");
