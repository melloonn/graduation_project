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
    </div>
    <div class="main-content">
      <div
        class="indicators-div"
        tabindex="0"
        @click="navigateTo('/indicators')"
      >
        <p>// INDICATORS</p>
      </div>
      <div class="category-div" tabindex="0" @click="navigateTo('/category')">
        <p>// CATEGORY</p>
      </div>
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
    const storedDarkMode = localStorage.getItem("isDarkMode");
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
.dark-mode-logo {
  color: #75fb9f; /* 暗模式顏色 */
}

.main-content {
  width: 100%;
  flex: 1;
  /* height: 82vh; */
  display: flex;
  gap: 1rem;
  padding-top: 1rem;
  justify-content: center;
}

.indicators-div {
  position: relative;
  width: 529px;
  height: 591px;
  display: flex;
  align-items: flex-end;
  padding-bottom: 0.25rem;
  padding-left: 0.5rem;
  cursor: pointer;
}

.indicators-div::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("../images/Forex Trading Backdrop_0.jpg");
  background-size: cover;
  background-position: center;
  filter: grayscale(100%);
  z-index: 0; /* 確保背景在底層 */
}

.category-div {
  position: relative;
  width: 529px;
  height: 591px;
  display: flex;
  align-items: flex-end;
  padding-bottom: 0.25rem;
  padding-left: 0.5rem;
  cursor: pointer;
}

.category-div::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("../images/Pin page image_0.jpg");
  background-size: cover;
  background-position: center;
  filter: grayscale(100%) brightness(0.65);
  z-index: 0; /* 確保背景在底層 */
}

/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}

p {
  position: relative;
  z-index: 1;
  margin: 0;
  font-family: "fonts8", sans-serif;
  font-style: normal;
  font-size: 24px;
  user-select: none;
  color: #75fb9f;
}

@font-face {
  font-family: "fonts8";
  src: url("../assets/fonts/8-BIT-WONDER.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
</style>
