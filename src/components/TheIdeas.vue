<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <div class="header">
      <div
        :class="['logo', { 'dark-mode-logo': isDarkMode }]"
        @click="navigateTo('/main')"
      >
        <svg
          width="95"
          height="39"
          viewBox="0 0 95 39"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M0 18.1048V38.0911C5.96995 38.3507 14.1566 38.2183 20.2459 36.2742C26.6156 34.2392 33.7432 30.0447 37.3771 25.8917V38.0911C44.1257 38.0911 49.5765 38.6102 59.1803 35.7551C65.2645 33.9459 71.1202 29.7851 75.2732 25.8917V38.0911H95V0.973633C88.2514 1.2332 87.1846 0.893168 80.9836 2.01188C65.1503 4.34795 63.881 13.3418 57.623 14.4709V1.2332C57.623 1.2332 42.5683 0.454507 34.2623 4.86708C23.8772 10.3854 18.6885 19.9217 0 18.1048Z"
            :fill="isDarkMode ? 'black' : '#75FB9F'"
          />
          <path
            d="M16 8C10.6667 9.472 9.472 10.6667 8 16C6.528 10.6667 5.33333 9.472 0 8C5.33333 6.528 6.528 5.33333 8 0C9.472 5.33333 10.6667 6.528 16 8Z"
            :fill="isDarkMode ? 'black' : '#75FB9F'"
          />
        </svg>
      </div>
      <div class="back-btn">
        <svg
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          @click="navigateTo('/main')"
        >
          <path
            d="M28.3333 18.333V16.6663H26.6667V14.9997H23.3333V11.6663H20V8.33301H16.6667V4.99967H13.3333V3.33301H10V8.33301H13.3333V11.6663H16.6667V14.9997H20V18.333H23.3333V21.6663H20V24.9997H16.6667V28.333H13.3333V31.6663H10V36.6663H13.3333V34.9997H16.6667V31.6663H20V29.9997V28.333H23.3333V26.6663V24.9997H26.6667V23.333H28.3333V21.6663H30V19.9997V18.333H28.3333Z"
            :fill="isDarkMode ? 'white' : 'black'"
          />
        </svg>
      </div>
    </div>
    <div class="container">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isDarkMode: false,
    };
  },
  components: {},
  mounted() {
    const storedDarkMode = sessionStorage.getItem("isDarkMode");
    if (storedDarkMode !== null) {
      this.$isDarkMode = JSON.parse(storedDarkMode);
      this.$nextTick(() => {
        console.log(this.$isDarkMode);
      });
      console.log(this.$isDarkMode);
    }
    if (this.$isDarkMode == true) {
      this.isDarkMode = true;
    }
  },
  methods: {
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.$router.push(path);
    },
  },
};
</script>

<style scoped>
.full {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #75fb9f;
}
/* header */
.header {
  position: relative;
  justify-content: center;
  align-items: center;
  height: 16vh;
  width: 100%;
  display: flex;
}
.logo {
  border-radius: 10px;
  background-color: #1b2023;
  width: 12vw;
  height: 8.15vh;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  cursor: pointer;
}
.back-btn {
  right: 65px;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
  cursor: pointer;
}

/* From Uiverse.io by musashi-13 */
.container {
  width: 100%;
  height: 100%;
}

.container div {
  position: absolute;
  height: 238px;
  width: 337px;
  background-color: #ffffff;
  border: 2px solid #000000;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  border-radius: 30px;
  transform-origin: bottom left;
  scale: 1;
  transition-duration: 200ms;
}

.container div:hover {
  scale: 1.1;
}

.container div:nth-child(n) {
  transform: rotate(0deg) translate(0px, -8px);
}

.container:hover div:nth-child(1) {
  transform: rotate(-54deg) translate(0px, -8px);
}
.container:hover div:nth-child(2) {
  transform: rotate(-36deg) translate(0px, -8px);
}
.container:hover div:nth-child(3) {
  transform: rotate(-18deg) translate(0px, -8px);
}
.container:hover div:nth-child(4) {
  transform: rotate(0deg) translate(0px, -8px);
}
.container:hover div:nth-child(5) {
  transform: rotate(18deg) translate(0px, -8px);
}
.container:hover div:nth-child(6) {
  transform: rotate(36deg) translate(0px, -8px);
}
.container:hover div:nth-child(7) {
  transform: rotate(54deg) translate(0px, -8px);
}

.dark-mode-logo {
  background-color: #75fb9f; /* 暗模式顏色 */
}
/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}
</style>
