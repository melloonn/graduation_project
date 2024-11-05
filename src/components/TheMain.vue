<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <div class="header">
      <div class="logo">
        <svg
          width="95"
          height="39"
          viewBox="0 0 95 39"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M0 18.1048V38.0911C5.96995 38.3507 14.1566 38.2183 20.2459 36.2742C26.6156 34.2392 33.7432 30.0447 37.3771 25.8917V38.0911C44.1257 38.0911 49.5765 38.6102 59.1803 35.7551C65.2645 33.9459 71.1202 29.7851 75.2732 25.8917V38.0911H95V0.973633C88.2514 1.2332 87.1846 0.893168 80.9836 2.01188C65.1503 4.34795 63.881 13.3418 57.623 14.4709V1.2332C57.623 1.2332 42.5683 0.454507 34.2623 4.86708C23.8772 10.3854 18.6885 19.9217 0 18.1048Z"
            fill="black"
          />
          <path
            d="M16 8C10.6667 9.472 9.472 10.6667 8 16C6.528 10.6667 5.33333 9.472 0 8C5.33333 6.528 6.528 5.33333 8 0C9.472 5.33333 10.6667 6.528 16 8Z"
            fill="black"
          />
        </svg>
      </div>
      <div class="stock" :class="{ 'stock-dark-mode': isDarkMode }">
        <div class="marquee-container">
          <div class="marquee-text">
            AAPL: 275.33 META: 500.12 GOOG: 754.56 TSLA: 1548.21 MFJ: null
          </div>
        </div>
      </div>
      <div class="time" @click="navigateTo('/profile')" tabindex="0">
        <svg
          class="user-div"
          width="46"
          height="46"
          viewBox="0 0 46 46"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M15.3334 23H17.25V24.9167H28.75V23H30.6667V21.0833H32.5834V9.58333H30.6667V7.66667H28.75V5.75H17.25V7.66667H15.3334V9.58333H13.4167V21.0833H15.3334V23ZM17.25 13.4167H19.1667V11.5H21.0834V9.58333H24.9167V11.5H26.8334V13.4167H28.75V17.25H26.8334V19.1667H24.9167V21.0833H21.0834V19.1667H19.1667V17.25H17.25V13.4167Z"
            fill="black"
          />
          <path
            d="M36.4167 30.6663V28.7497H34.5V26.833H11.5V28.7497H9.58335V30.6663H7.66669V40.2497H11.5V34.4997H13.4167V32.583H15.3334V30.6663H30.6667V32.583H32.5834V34.4997H34.5V40.2497H38.3334V30.6663H36.4167Z"
            fill="black"
          />
        </svg>
      </div>
    </div>
    <div class="main-content">
      <!-- <div class="svg-container"></div> -->
      <the-main-page :is-dark-mode="isDarkMode"></the-main-page>
    </div>
  </div>
</template>
<script>
import TheMainPage from "./accessories/TheMainPage.vue";
export default {
  data() {
    return {
      isDarkMode: false,
    };
  },
  components: {
    TheMainPage,
  },
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
/* header */
.header {
  gap: 1.75rem;
  justify-content: center;
  padding: 1rem 3.15rem;
  align-items: center;
  height: 18vh;
  width: 100%;
  display: flex;
}

.logo {
  border-radius: 10px;
  background-color: #75fb9f;
  width: 12vw;
  height: 8.15vh;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}
.stock {
  border-radius: 10px;
  background-color: #1b2023;
  color: #75fb9f;
  width: 53vw;
  height: 8.15vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stock-dark-mode {
  background-color: #75fb9f;
  color: #1b2023;
}
.marquee-container {
  overflow: hidden;
  white-space: nowrap;
  width: 100%;
}

.marquee-text {
  display: inline-block;
  padding-left: 100%;
  animation: marquee 60s linear infinite;
}

@keyframes marquee {
  from {
    transform: translateX(0%);
  }
  to {
    transform: translateX(-100%);
  }
}

.time {
  border-radius: 100px;
  background-color: #75fb9f;
  width: 18vw;
  height: 8vh;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 1.5rem;
}
.user-div {
  display: flex;
}

.svg-container {
  width: 100%;
  height: 73vh;
  background-image: url("../assets/Main.svg");
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  margin: 0.3rem 4.6rem 0 4.6rem;
}

.footer-text {
  grid-column: 1 / -1; /* 佔滿所有列 */
  text-align: center; /* 文字置中 */
}
@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/Minecraft.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "PressStar2PFont";
  src: url("../assets/fonts/PressStart2P-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

p {
  margin: 0;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 2rem;
  user-select: none;
}

.marquee-text {
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 300;
  font-size: 1.5rem;
  user-select: none;
}

.full {
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.main-content {
  width: 100%;
  /* height: 82vh; */
  display: flex;
  justify-content: center;
  align-items: center;
}
/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}

/* 當視窗寬度大於1600px */
/* @media (min-width: 1600px) {
    .svg-container {
      background-image: radial-gradient(circle, black 3.6px, transparent 3.6px);
      background-size: 36px 36px;
    }
  } */

/* 當視窗寬度在1400px到1600px之間 */
/* @media (min-width: 1400px) and (max-width: 1599px) {
    .svg-container {
      background-image: radial-gradient(circle, black 3.3px, transparent 3.3px);
      background-size: 34px 34px;
    }
  } */

/* 當視窗寬度在1000px到1300px之間 */
/* @media (min-width: 1000px) and (max-width: 1299px) {
    .svg-container {
      background-image: radial-gradient(circle, black 3px, transparent 3px);
      background-size: 30px 30px;
    }
  } */
</style>
