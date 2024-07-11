import { createApp } from "vue";
import App from "./App.vue";
// import TheLoginVue from "./components/TheLogin.vue";
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
app.component("font-awesome-icon", FontAwesomeIcon);
// app.component("the-login", TheLoginVue);

app.use(ElementPlus);
app.use(router);

app.mount("#app");
