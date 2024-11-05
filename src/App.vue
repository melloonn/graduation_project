<template>
  <Transition name="fade-slide">
    <router-view />
  </Transition>
</template>

<script>
export default {
  name: "App",
  components: {},
  // created() {
  //   // 設定一個定時器，每 5 分鐘檢查一次 token
  //   this.tokenCheckInterval = setInterval(() => {
  //     this.checkTokenValidity();
  //   }, 5 * 60 * 1000); // 每 5 分鐘
  // },
  // methods: {
  //   checkTokenValidity() {
  //     const accessToken = sessionStorage.getItem("access");
  //     const refreshToken = sessionStorage.getItem("refresh");

  //     if (
  //       this.isTokenExpired(accessToken) &&
  //       this.isTokenExpired(refreshToken)
  //     ) {
  //       // 如果兩個 token 都失效，則強制登出
  //       this.forceLogout();
  //     }
  //   },
  //   isTokenExpired(token) {
  //     if (!token) return true;
  //     const payload = JSON.parse(atob(token.split(".")[1])); // 解碼 JWT 的 payload
  //     const expiry = payload.exp * 1000; // token 過期時間 (毫秒)
  //     const now = Date.now(); // 當前時間 (毫秒)
  //     return now > expiry; // 如果當前時間大於過期時間，表示 token 已失效
  //   },
  //   forceLogout() {
  //     sessionStorage.removeItem("access");
  //     sessionStorage.removeItem("refresh");
  //     this.$router.push("/home");
  //     clearInterval(this.tokenCheckInterval); // 停止定時器
  //     this.$message({
  //       message: "已登出，請重新登入。",
  //       type: "error",
  //     });
  //   },
  // },
  // beforeDestroy() {
  //   if (this.tokenCheckInterval) {
  //     clearInterval(this.tokenCheckInterval);
  //   }
  // },
};
</script>

<style>
.fade-slide-enter-active {
  transition: opacity 0.5s ease, transform 1s ease;
}

.fade-slide-enter {
  transition: opacity 0.5s ease, transform 1s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transition: opacity 1s ease-out, transform 1s ease;
}
</style>
