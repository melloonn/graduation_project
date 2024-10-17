<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <!-- header  -->
    <div class="header">
      <div class="back-btn">
        <svg
          @click="navigateTo('/enterprise_selection')"
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M26.6667 3.3335V5.00016H23.3333V8.3335H20V11.6668H16.6667V15.0002H13.3333V16.6668H11.6667V18.3335H10V21.6668H11.6667V23.3335H13.3333V25.0002H16.6667V28.3335H20V31.6668H21.6667H23.3333V33.3335V35.0002H26.6667V36.6668H30V31.6668H26.6667V28.3335H23.3333V25.0002H20V21.6668H16.6667V18.3335H20V15.0002H23.3333V11.6668H26.6667V8.3335H30V3.3335H26.6667Z"
            fill="black"
          />
        </svg>
      </div>
      <div class="logo">
        <svg
          @click="navigateTo('/main')"
          style="cursor: pointer"
          width="60"
          height="25"
          viewBox="0 0 60 25"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M0 11.4349V24.0579C3.77049 24.2218 8.94098 24.1382 12.7869 22.9103C16.8098 21.6251 21.3115 18.9759 23.6066 16.3529V24.0579C27.8689 24.0579 31.3115 24.3857 37.377 22.5824C41.2197 21.4398 44.918 18.812 47.541 16.3529V24.0579H60V0.615234C55.7377 0.779169 55.0639 0.564415 51.1475 1.27097C41.1475 2.74638 40.3459 8.42671 36.3934 9.13982V0.779169C36.3934 0.779169 26.8852 0.287366 21.6393 3.07425C15.0803 6.5595 11.8033 12.5824 0 11.4349Z"
            :fill="isDarkMode ? 'black' : 'black'"
          />
          <path
            d="M10.1053 5.05263C6.73684 5.98232 5.98232 6.73684 5.05263 10.1053C4.12295 6.73684 3.36842 5.98232 0 5.05263C3.36842 4.12295 4.12295 3.36842 5.05263 0C5.98232 3.36842 6.73684 4.12295 10.1053 5.05263Z"
            :fill="isDarkMode ? 'black' : 'black'"
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
      <!-- enterprise  -->
      <div class="main-div">
        <div class="main-div-org" v-if="showMainDiv">
          <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">ENTERPRISE</p>
          <div class="select-button">
            <svg
              @click="toggleEnterprise"
              style="cursor: pointer"
              width="60"
              height="60"
              viewBox="0 0 60 60"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
                stroke="black"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M30 40L40 30L30 20"
                stroke="black"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M20 30H40"
                stroke="black"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
        </div>
        <div class="button-list main-div-expand" v-if="isEmterprisePressed">
          <div class="scrollable-list">
            <div
              v-for="item in financialItems"
              :key="item.name"
              @click="handleClick(item)"
              class="financial-button list-div"
              tabindex="0"
            >
              {{ item.name }}
            </div>
          </div>
        </div>
      </div>
      <!-- finacial sheet  -->
      <div class="main-div" v-if="showMainDiv">
        <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">
          FINANCIAL SHEET
        </p>
        <div class="select-button">
          <svg
            style="cursor: pointer"
            width="60"
            height="60"
            viewBox="0 0 60 60"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
              stroke="black"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M30 40L40 30L30 20"
              stroke="black"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M20 30H40"
              stroke="black"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
      </div>
      <!-- indicator  -->
      <div class="main-div" v-if="showMainDiv">
        <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">INDICATORS</p>
        <div class="select-button">
          <svg
            style="cursor: pointer"
            width="60"
            height="60"
            viewBox="0 0 60 60"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
              stroke="black"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M30 40L40 30L30 20"
              stroke="black"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M20 30H40"
              stroke="black"
              stroke-width="3"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import anime from "animejs/lib/anime.es.js";
export default {
  data() {
    return {
      showMainDiv: true,
      isEmterprisePressed: false,
      isFinacialPressed: false,
      isIndicatorPressed: false,
      isAnimating: false,
      isDarkMode: false,
      svgWidth: 1231,
      svgHeight: 346,
      viewBox: "0 0 1231 346",
      pathData:
        "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z",
      financialItems: [
        { name: "華南金HNFHC" },
        { name: "富邦金FUBFH" },
        { name: "國泰金CFH" },
        { name: "開發金KGI" },
        { name: "玉山金ESFHC" },
        { name: "元大金YFH" },
        { name: "兆豐金MFG" },
        { name: "台新金TSFHC" },
        { name: "新光金SKFH" },
        { name: "國票金CBFHC" },
        { name: "永豐金SPH" },
        { name: "中信金CTBC" },
        { name: "第一金FFHC" },
        { name: "日盛金JSFHC" },
        { name: "合庫金TCFHC" },
      ],
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
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.$router.push(path);
    },
    toggleEnterprise() {
      this.isEmterprisePressed = !this.isEmterprisePressed;
      this.showMainDiv = false;
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
.main-div {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  border: 1px solid black;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.main-div-org {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.main-div-expand {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.select-button {
  position: absolute;
  right: 80px;
}

/* enterprise-list  */
.button-list {
  width: 250px;
  height: 390px;
  overflow-y: auto;
  margin: 15px;
  box-sizing: border-box;
  z-index: 10;
}
.button-list::-webkit-scrollbar {
  display: none;
}
.scrollable-list {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.financial-button {
}

.financial-button:hover {
  color: #75fb9f;
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
.list-div {
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 200%;
  user-select: none;
  letter-spacing: 0.5em;
  /* color: white; */
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
@font-face {
  font-family: "Inter";
  src: url("../assets/fonts/Inter.ttf") format("truetype");
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
