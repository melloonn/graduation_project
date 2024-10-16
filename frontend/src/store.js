// src/store.js
import { reactive } from "vue";

export const store = reactive({
  darkMode: false,
  toggleDarkMode() {
    console.log("Toggle dark mode"); // 添加调试信息
    this.darkMode = !this.darkMode;
    console.log("Dark mode:", this.darkMode); // 添加调试信息
  },
});
