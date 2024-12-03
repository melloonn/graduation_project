<template>
  <div class="unity-container">
    <!-- header  -->
    <div class="header">
      <div class="back-btn">
        <svg
          @click="navigateTo('/main')"
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M26.6667 3.3335V5.00016H23.3333V8.3335H20V11.6668H16.6667V15.0002H13.3333V16.6668H11.6667V18.3335H10V21.6668H11.6667V23.3335H13.3333V25.0002H16.6667V28.3335H20V31.6668H21.6667H23.3333V33.3335V35.0002H26.6667V36.6668H30V31.6668H26.6667V28.3335H23.3333V25.0002H20V21.6668H16.6667V18.3335H20V15.0002H23.3333V11.6668H26.6667V8.3335H30V3.3335H26.6667Z"
            fill="#75fb9f"
          />
        </svg>
      </div>
      <div class="logo">
        <svg
          width="60"
          height="25"
          viewBox="0 0 60 25"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          @click="navigateTo('/main')"
          style="cursor: pointer"
        >
          <path
            d="M0 11.4349V24.0579C3.77049 24.2218 8.94098 24.1382 12.7869 22.9103C16.8098 21.6251 21.3115 18.9759 23.6066 16.3529V24.0579C27.8689 24.0579 31.3115 24.3857 37.377 22.5824C41.2197 21.4398 44.918 18.812 47.541 16.3529V24.0579H60V0.615234C55.7377 0.779169 55.0639 0.564415 51.1475 1.27097C41.1475 2.74638 40.3459 8.42671 36.3934 9.13982V0.779169C36.3934 0.779169 26.8852 0.287366 21.6393 3.07425C15.0803 6.5595 11.8033 12.5824 0 11.4349Z"
            fill="#75fb9f"
          />
          <path
            d="M10.1053 5.05263C6.73684 5.98232 5.98232 6.73684 5.05263 10.1053C4.12295 6.73684 3.36842 5.98232 0 5.05263C3.36842 4.12295 4.12295 3.36842 5.05263 0C5.98232 3.36842 6.73684 4.12295 10.1053 5.05263Z"
            fill="#75fb9f"
          />
        </svg>
      </div>
    </div>
    <iframe src="/Unity/index.html" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name: "UnityGame",
  methods: {
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.shouldAutoScroll = false;
      this.$router.push(path);
    },
  },
  mounted() {},
};
</script>

<style scoped>
.unity-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 充滿整個視窗的高度 */
  width: 100vw; /* 充滿整個視窗的寬度 */
  background-color: #231f20;
}

iframe {
  border: none; /* 去掉邊框 */
  width: 100%;
  flex: 1;
}
/* header */
.header {
  position: relative;
  justify-content: center;
  align-items: center;
  height: 6.25vh;
  width: 100%;
  display: flex;
  border: 1px solid black;
}

.back-btn {
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
  cursor: pointer;
}
.logo {
  border-radius: 10px;
  width: 12vw;
  height: 8.15vh;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}
</style>
