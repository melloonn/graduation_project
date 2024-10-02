<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <div class="header">
      <div class="logo">
        <svg
          width="60"
          height="25"
          viewBox="0 0 60 25"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M0 11.4349V24.0579C3.77049 24.2218 8.94098 24.1382 12.7869 22.9103C16.8098 21.6251 21.3115 18.9759 23.6066 16.3529V24.0579C27.8689 24.0579 31.3115 24.3857 37.377 22.5824C41.2197 21.4398 44.918 18.812 47.541 16.3529V24.0579H60V0.615234C55.7377 0.779169 55.0639 0.564415 51.1475 1.27097C41.1475 2.74638 40.3459 8.42671 36.3934 9.13982V0.779169C36.3934 0.779169 26.8852 0.287366 21.6393 3.07425C15.0803 6.5595 11.8033 12.5824 0 11.4349Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
          <path
            d="M10.1053 5.05263C6.73684 5.98232 5.98232 6.73684 5.05263 10.1053C4.12295 6.73684 3.36842 5.98232 0 5.05263C3.36842 4.12295 4.12295 3.36842 5.05263 0C5.98232 3.36842 6.73684 4.12295 10.1053 5.05263Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
        </svg>
      </div>
    </div>
    <div class="chatbox">
      <svg
        width="1231"
        height="346"
        viewBox="0 0 1231 346"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z"
          :fill="isDarkMode ? '#1C1F1C' : 'white'"
          :stroke="isDarkMode ? '#A7A9AC' : '#1463F3'"
          stroke-width="5"
        />
      </svg>
    </div>
    <div class="main-content">
      <div>
        <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">ENTERPRISE</p>
      </div>
      <div>
        <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">
          FINANCIAL SHEET
        </p>
      </div>
      <div>
        <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">INDICATORS</p>
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
  methods: {},
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
  height: 6.25vh;
  width: 100%;
  display: flex;
  border: 1px solid black;
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

.chatbox {
  padding: 1rem 0.5rem 0.5rem 0.5rem;
  justify-content: center;
  align-items: center;
  height: auto;
  width: 100%;
  display: flex;
  border: 1px solid black;
}
.main-content {
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.main-content div {
  flex: 1;
  text-align: center;
  justify-content: center;
  align-content: center;
  border: 1px solid black;
}
/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}
.dark-mode border {
  border: 2px solid #75fb9f;
}

p {
  margin: 0;
  font-family: "Micro5", sans-serif;
  font-style: normal;
  font-weight: 300;
  font-size: 96px;
  user-select: none;
}

@font-face {
  font-family: "Micro5";
  src: url("../assets/fonts/Micro5-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
</style>
