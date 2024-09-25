<template>
  <!-- Homepage -->
  <div :class="{ 'dark-mode': isDarkMode }" class="light-mode full">
    <!-- Header 部分 -->
    <div
      class="header d-flex justify-content-end align-items-center position-relative"
    >
      <div class="d-flex btnGroup align-items-center">
        <div class="mr-5">
          <the-menu-btn :is-dark-mode="isDarkMode"></the-menu-btn>
        </div>
        <div class="mr-5">
          <the-sun-moon-btn
            @toggle-dark-mode="handleToggleDarkMode"
          ></the-sun-moon-btn>
        </div>
      </div>
    </div>
    <!-- 中間部分 -->
    <!-- Create -->
    <div class="position-relative mid-container flex-grow-1">
      <div class="title position-relative">
        <div class="create-position">
          <h1 class="display-1">CREATES</h1>
          <!-- Arrow-->
        </div>
        <div v-if="!isDarkMode" class="arrow-position svg-container">
          <transition-group name="fade" tag="arrowA">
            <svg
              class="img-fluid"
              viewBox="0 0 90 90"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g id="Group 18" style="mix-blend-mode: multiply">
                <rect
                  id="Rectangle 2510"
                  x="50"
                  y="50"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2512"
                  x="20"
                  y="20"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2554"
                  x="10"
                  y="10"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect id="Rectangle 2555" width="10" height="10" fill="black" />
                <rect
                  id="Rectangle 2513"
                  x="80"
                  y="80"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2526"
                  x="60"
                  y="80"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2527"
                  x="70"
                  y="80"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2516"
                  x="60"
                  y="60"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2518"
                  x="30"
                  y="30"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2519"
                  x="80"
                  y="70"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2522"
                  x="70"
                  y="70"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2524"
                  x="40"
                  y="40"
                  width="10"
                  height="10"
                  fill="black"
                />
                <rect
                  id="Rectangle 2525"
                  x="80"
                  y="60"
                  width="10"
                  height="10"
                  fill="black"
                />
              </g>
            </svg>
          </transition-group>
        </div>
        <div v-else class="arrow-position svg-container">
          <transition-group name="fade" tag="arrowB">
            <svg
              class="img-fluid"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 90 90"
              fill="none"
            >
              <rect x="50" y="50" width="10" height="10" fill="white" />
              <rect x="20" y="20" width="10" height="10" fill="white" />
              <rect x="10" y="10" width="10" height="10" fill="white" />
              <rect width="10" height="10" fill="white" />
              <rect x="80" y="80" width="10" height="10" fill="white" />
              <rect x="60" y="80" width="10" height="10" fill="white" />
              <rect x="70" y="80" width="10" height="10" fill="white" />
              <rect x="60" y="60" width="10" height="10" fill="white" />
              <rect x="30" y="30" width="10" height="10" fill="white" />
              <rect x="80" y="70" width="10" height="10" fill="white" />
              <rect x="70" y="70" width="10" height="10" fill="white" />
              <rect x="40" y="40" width="10" height="10" fill="white" />
              <rect x="80" y="60" width="10" height="10" fill="white" />
            </svg>
          </transition-group>
        </div>
        <!-- NewEra -->
        <div class="button-container">
          <the-new-era
            :is-dark-mode="isDarkMode"
            class="era-position"
          ></the-new-era>
        </div>
        <!-- Investment  -->
        <div class="investment-position">
          <p class="lead">of</p>
          <h1 class="display-1">{ INVESTMENT }</h1>
        </div>
      </div>
      <!-- Square -->
      <div v-if="!isDarkMode" class="square-position flex-grow-1">
        <transition-group name="fade">
          <svg
            class="img-fluid square-svg"
            viewBox="0 0 1280 300"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <rect y="100" width="98.4615" height="100" fill="#75FB9F" />
            <rect x="98.4614" width="98.4615" height="100" fill="black" />
            <rect
              x="98.4614"
              y="200"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="196.923"
              y="100"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="295.385"
              y="100"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="590.769"
              y="200"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="689.231"
              y="100"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect x="886.154" width="98.4615" height="100" fill="#A7A9AC" />
            <rect
              x="1083.08"
              y="200"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect x="1083.08" width="98.4615" height="100" fill="#A7A9AC" />
            <rect
              x="196.923"
              y="200"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect
              x="295.385"
              y="200"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect
              x="393.846"
              y="100"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect x="590.769" width="98.4615" height="100" fill="black" />
            <rect
              x="787.692"
              y="100"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect
              x="984.615"
              y="100"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect
              x="1181.54"
              y="100"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect
              x="787.692"
              y="200"
              width="98.4615"
              height="100"
              fill="black"
            />
            <rect x="393.846" width="98.4615" height="100" fill="#75FB9F" />
            <rect x="492.308" width="98.4615" height="100" fill="#75FB9F" />
            <rect
              x="492.308"
              y="100"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect x="689.231" width="98.4615" height="100" fill="#75FB9F" />
            <rect
              x="689.231"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect x="984.615" width="98.4615" height="100" fill="#75FB9F" />
            <rect
              x="1181.54"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect
              x="886.154"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect
              x="393.846"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
          </svg>
        </transition-group>
      </div>
      <div v-else class="square-position flex-grow-1">
        <transition-group name="fade">
          <svg
            class="img-fluid square-svg"
            viewBox="0 0 1280 300"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <rect y="100" width="98.4615" height="100" fill="#75FB9F" />
            <rect x="98.4615" width="98.4615" height="100" fill="white" />
            <rect
              x="98.4615"
              y="200"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="196.923"
              y="100"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="295.385"
              y="100"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="590.769"
              y="200"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect
              x="689.231"
              y="100"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect x="886.154" width="98.4615" height="100" fill="#A7A9AC" />
            <rect
              x="1083.08"
              y="200"
              width="98.4615"
              height="100"
              fill="#A7A9AC"
            />
            <rect x="1083.08" width="98.4615" height="100" fill="#A7A9AC" />
            <rect
              x="196.923"
              y="200"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect
              x="295.385"
              y="200"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect
              x="393.846"
              y="100"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect x="590.769" width="98.4615" height="100" fill="white" />
            <rect
              x="787.692"
              y="100"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect
              x="984.615"
              y="100"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect
              x="1181.54"
              y="100"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect
              x="787.692"
              y="200"
              width="98.4615"
              height="100"
              fill="white"
            />
            <rect x="196.923" width="98.4615" height="100" fill="#75FB9F" />
            <rect x="393.846" width="98.4615" height="100" fill="#75FB9F" />
            <rect x="492.308" width="98.4615" height="100" fill="#75FB9F" />
            <rect
              x="492.308"
              y="100"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect x="689.231" width="98.4615" height="100" fill="#75FB9F" />
            <rect
              x="689.231"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect x="984.615" width="98.4615" height="100" fill="#75FB9F" />
            <rect
              x="1181.54"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect
              x="886.154"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
            <rect
              x="393.846"
              y="200"
              width="98.4615"
              height="100"
              fill="#75FB9F"
            />
          </svg>
        </transition-group>
      </div>
    </div>
  </div>
  <!-- Menu section -->
  <div></div>
</template>

<script>
import TheMenuBtn from "./accessories/TheMenuBtn.vue";
import TheSunMoonBtn from "./accessories/TheSunMoonBtn.vue";
import TheNewEra from "./accessories/TheNewEra.vue";

export default {
  data() {
    return {
      isDarkMode: false, // 主頁面中的 darkMode 狀態
    };
  },
  components: {
    TheMenuBtn,
    TheSunMoonBtn,
    TheNewEra,
  },
  methods: {
    handleToggleDarkMode(darkMode) {
      // 接收子組件傳來的 darkMode 狀態，並更新到主頁面中的狀態
      this.isDarkMode = darkMode;
      // 在這裡可以做相應的樣式或主題切換操作
    },
  },
};
</script>

<style scoped>
.button-container {
  left: 78%;
  top: 28%;
  position: fixed;
  animation: floatAnimation 1.5s ease-in-out infinite alternate;
  z-index: 2;
}

@keyframes floatAnimation {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-15px);
  }
}
.title {
  width: 100%;
  height: calc(62vh - 5rem);
  display: flex;
  justify-content: center;
  align-items: center;
}
.mid-container {
  /* flex: 1 1 0%; */
  width: 100%;
  display: flex;
  flex-direction: column;
}
.full {
  width: 100vw;
  height: 100vh;
  flex-direction: column;
  margin: 0;
  padding: 0;
  display: flex;
}
.btnGroup {
  height: 100%;
  padding-right: 30px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/MinecraftRegular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

/* 可根据需要添加自定义样式 */
.header {
  height: 5rem; /* 让 header 高度占满整个视窗 */
  width: 100%;
}

h1 {
  display: inline-block;
  white-space: nowrap;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 5.5rem;
  user-select: none;
}
p {
  padding-right: 1.3rem;
  /* margin-bottom: 0.5rem; */
  display: inline-block;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 2rem;
  user-select: none;
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

.svg-container {
  width: 6.5%; /* 或者您想設置的其他寬度 */
  height: auto;
}

.square-svg {
  width: 100%;
  height: auto;
  display: block;
}

.create-position {
  position: absolute;
  top: 5%; /* 根据需要调整位置 */
  left: 12%;
  /* padding: 1rem; */
}

.arrow-position {
  position: absolute;
  top: 25%; /* 调整位置与“a”对齐 */
  left: 50%;
}

.era-position {
}
.investment-position {
  position: absolute;
  bottom: 0%; /* 根据需要调整位置 */
  left: 18%;
}
.square-position {
  position: relative;
  width: 100%;
  height: calc(38vh - 5rem); /* 确保容器撑满父容器 */
  display: flex;
  justify-content: flex-end; /* 使内容靠右对齐 */
  align-items: flex-end; /* 使内容靠底部对齐 */
  overflow: hidden;
  z-index: 0;
}

/* Light-Mode */
.light-mode {
  transition: ease-out 0.3s;
}

/* Dark-Mode */
.dark-mode {
  background-color: black;
  color: white;
  transition: ease-out 0.3s;
}

@media (max-width: 768px) {
  .create-position {
    left: 5%; /* 在較小的螢幕寬度下調整位置 */
    top: 5vh; /* 在較小的螢幕高度下調整位置 */
  }

  .arrow-position {
    left: 42%; /* 在較小的螢幕寬度下調整位置 */
    top: 10.5vh; /* 在較小的螢幕高度下調整位置 */
  }
  .era-position {
    left: 70%;
    top: 11vh;
  }
  h1 {
    font-size: 2rem;
  }
}
</style>
