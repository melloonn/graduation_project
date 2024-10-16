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

    <div class="chatbox" :style="{ height: isAnimating ? '100vh' : '365px' }">
      <svg
        :width="svgWidth"
        :height="svgHeight"
        :viewBox="viewBox"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          :d="pathData"
          :fill="isDarkMode ? '#1C1F1C' : 'white'"
          :stroke="isDarkMode ? '#A7A9AC' : '#1463F3'"
          stroke-width="5"
        />
        <foreignObject x="0" y="0" width="100%" height="100%">
          <div class="enlarge-btn" @click="startAnimation">
            <svg
              width="25"
              height="25"
              viewBox="0 0 25 25"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M15.625 3.125H21.875V9.375"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M9.375 21.875H3.125V15.625"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M21.8752 3.125L14.5835 10.4167"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M3.125 21.8747L10.4167 14.583"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
          <div xmlns="http://www.w3.org/1999/xhtml" class="text-block">
            <h3 :style="{ color: isDarkMode ? '#A7A9AC' : 'black' }">
              Your summary text here
            </h3>
          </div>
        </foreignObject>
      </svg>
    </div>

    <div class="main-content" v-show="!isAnimating">
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
import anime from "animejs/lib/anime.es.js";
export default {
  data() {
    return {
      isAnimating: false,
      isDarkMode: false,
      svgWidth: 1231,
      svgHeight: 346,
      viewBox: "0 0 1231 346",
      pathData:
        "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z",
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
    startAnimation() {
      this.isAnimating = !this.isAnimating;
      if (this.isAnimating) {
        anime({
          targets: this,
          // svgWidth: 1231,
          svgHeight: 727,
          viewBox: [
            { value: "0 0 1231 346" }, // 開始 viewBox
            { value: "0 0 1231 727" }, // 結束 viewBox
          ],
          pathData: [
            {
              value:
                "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z",
            }, // 開始 path
            {
              value:
                "M3 103.92L77.4696 3H1196.01L1227 564.964H1101.05L1156.53 719L1061.57 640.389L35.9865 679.694L3 103.92Z",
            }, // 結束 path
          ],
          easing: "easeInOutQuad",
          duration: 750,
        });
      }
      if (!this.isAnimating) {
        this.pathData =
          "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z";
        this.viewBox = "0 0 1231 346";
        this.svgHeight = "346";
      }
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
  position: relative;
  padding: 1rem 0.5rem 0.5rem 0.5rem;
  justify-content: center;
  align-items: center;
  width: 100%;
  display: flex;
  border: 1px solid black;
  transition: height 0.75s ease;
}

.output-box {
  width: 100%;
  height: auto;
  position: relative;
}

.svg-container {
  transform-origin: top; /* 缩放原点 */
}

.zoom-in {
  transform: scaleY(2); /* 垂直缩放 */
}

.enlarge-btn {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 1rem;
  margin-right: 3rem;
  cursor: pointer;
}

.text-block {
  display: flex;
  padding: 2rem 6rem 6rem 6rem;
  height: 100%;
  width: 100%;
  color: black;
  border-radius: 10px;
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

h3 {
  margin: 0;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 20px;
  user-select: none;
}

@font-face {
  font-family: "Micro5";
  src: url("../assets/fonts/Micro5-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "PressStar2PFont";
  src: url("../assets/fonts/PressStart2P-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

/* anime  */
.slide2-enter-active,
.slide2-leave-active {
  transition: all 0.75s ease;
}

.slide2-enter {
  transform: translateY(100%); /* 從下方進入 */
  opacity: 0; /* 透明開始 */
}

.slide2-enter-to {
  transform: translateY(0); /* 最終位置 */
  /* opacity: 1; 最終完全不透明 */
}
.slide2-leave {
  transform: translateY(0); /* 從當前位置開始 */
  /* opacity: 1;  */
}

.slide2-leave-to {
  transform: translateY(100%); /* 向下移動到下方 */
  /* opacity: 0; */
}
</style>
