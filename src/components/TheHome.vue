<template>
  <!-- Menu 部分 -->
  <div>
    <Transition name="slide">
      <the-menu
        class="menu-content"
        v-show="isMenuOpen"
        @close-menu="toggleMenu"
      ></the-menu>
    </Transition>
  </div>
  <!-- SignUp -->
  <div>
    <Transition name="fade-slide">
      <the-sign-up
        :is-dark-mode="isDarkMode"
        v-show="isLogInOpen"
        @close-logIn="toggleLogIn"
        class="LogIn-content"
      ></the-sign-up>
    </Transition>
  </div>
  <!--主頁-->
  <div :class="{ 'dark-mode': isDarkMode }" class="light-mode full">
    <!-- Header 部分 -->
    <div
      class="header d-flex justify-content-between align-items-center position-relative"
    >
      <div class="logo"><h3>LOGO</h3></div>
      <div class="d-flex btnGroup align-items-center">
        <div class="mr-3 menu-btn">
          <the-menu-btn
            class="menu"
            :is-dark-mode="isDarkMode"
            @click="toggleMenu"
          ></the-menu-btn>
        </div>
        <div class="mr-3">
          <the-sun-moon-btn
            class="sun-moon"
            @toggle-dark-mode="handleToggleDarkMode"
          ></the-sun-moon-btn>
        </div>
      </div>
    </div>
    <div class="position-relative mid-container flex-grow-1">
      <svg
        class="rec1"
        width="30"
        height="30"
        viewBox="0 0 30 30"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect width="30" height="30" :fill="currentRect" />
      </svg>
      <p class="text1">
        //Lorem ipsum <br />dolor sit<br />amet<br />consectetur.
      </p>
      <p class="text2">
        //malesuada tellus at eu eu. Id aliquet sed<br />morbi consectetur
        mollis consequat nibh. Vel<br />pretium sed sed facilisis leo non id.
      </p>
      <svg
        class="rec2"
        width="30"
        height="30"
        viewBox="0 0 30 30"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect width="30" height="30" :fill="currentRect" />
      </svg>
      <svg
        class="rec3"
        width="30"
        height="30"
        viewBox="0 0 30 30"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect width="30" height="30" :fill="currentRect" />
      </svg>

      <div class="start-btn">
        <svg
          class="img-fluid"
          viewBox="0 0 836 423"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
        >
          <path
            class="start"
            @click="toggleLogIn"
            d="M257.477 31.8287H114.823V237.065H2V379.584H228.21V321.115H437.957V421H673.923V321.115H780.625V237.065V185.904V137.592H834V2H594.46V101.854H257.477V31.8287Z"
            fill="url(#paint0_linear_538_115)"
            stroke="#A7A9AC"
            stroke-width="4"
          />
          <g class="startImage" clip-path="url(#clip0_538_115)">
            <rect
              x="185"
              y="129"
              width="466"
              height="165"
              fill="url(#pattern0_538_115)"
            />
          </g>
          <defs>
            <pattern
              id="pattern0_538_115"
              patternContentUnits="objectBoundingBox"
              width="1"
              height="1"
            >
              <use
                :xlink:href="currentUse"
                transform="scale(0.00462963 0.00884956)"
              />
            </pattern>
            <linearGradient
              id="paint0_linear_538_115"
              x1="573.896"
              y1="269.293"
              x2="134.85"
              y2="79.755"
              gradientUnits="userSpaceOnUse"
            >
              <stop id="stop1" class="gradient-stop" stop-color="#1B2023" />
              <stop
                id="stop2"
                class="gradient-stop"
                offset="1"
                stop-color="#788578"
              />
            </linearGradient>

            <image
              class="startImage"
              :id="currentImageId"
              width="216"
              height="113"
              :xlink:href="currentImageHref"
            />
          </defs>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
import TheMenuBtn from "./accessories/TheMenuBtn.vue";
import TheSunMoonBtn from "./accessories/TheSunMoonBtn.vue";
import TheNewEra from "./accessories/TheNewEra.vue";
import TheSignUp from "./TheSignUp.vue";
// import Menu from "./accessories/Menu.vue";
import TheMenu from "./TheMenu.vue";
export default {
  data() {
    return {
      currentRect: "#1C1F1C",
      currentImageId: "image0_538_115", // 初始图片 ID
      currentUse: "#image0_538_115",
      currentImageHref:
        "data:image/png;base64,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", // 初始图片 URL
      isFirstImage: true,
      isDarkMode: false, // 主頁面中的 darkMode 狀態
      isMenuOpen: false,
      isLogInOpen: false,
    };
  },
  components: {
    TheMenuBtn,
    TheSunMoonBtn,
    TheNewEra,
    TheMenu,
    TheSignUp,
  },
  watch: {
    isDarkMode(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.updateGradientColors();
      }
    },
  },
  methods: {
    handleToggleDarkMode(darkMode) {
      // 接收子組件傳來的 darkMode 狀態，並更新到主頁面中的狀態
      this.isDarkMode = darkMode;
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    toggleLogIn() {
      this.isLogInOpen = !this.isLogInOpen;
    },
    updateGradientColors() {
      const stop1 = document.getElementById("stop1");
      const stop2 = document.getElementById("stop2");

      if (this.isDarkMode) {
        this.currentRect = "#0fff50";
        this.currentImageId = "image0_562_188";
        this.currentUse = "#image0_562_188";
        this.currentImageHref =
          "data:image/png;base64,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";
        stop1.setAttribute("stop-color", "#75FB9F"); // Example dark mode color
        stop2.setAttribute("stop-color", "white");
        stop2.setAttribute("stop-opacity", "0.5"); // Example dark mode color
      } else {
        this.currentRect = "#1C1F1C";
        this.currentImageId = "image0_538_115";
        this.currentUse = "#image0_538_115";
        this.currentImageHref =
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANgAAABxCAYAAAC3M23LAAAACXBIWXMAAAMTAAADEwE9ZoPHAAAKcUlEQVR4nO2dW5IdJwyG26l4oV6EV+FFZKF+SB5SVBgiiV83Ln30VZ3CjLuREEhCzHj8PEVRFEVRFEVRWPn5+6+/b+7vZvf8b7NXURTFOiri+ih7FUVRRINGxt0tqu9qbrdfcTB1rPFR9vsATo24t0TkW+zH6VscwK5NxMk/nVOcrhCIPj5k1grtE9X3tJ9oL4/90PkWiew+3ty22JXBXsjKiHxSBK4MFpPBigXszlBeJ1rNKZlql1P9ETnYKlZG0rH99f3Ht74dvx4t7y16zfS8Qa/G7qD1KiKdtX2sfU/LzSebSKdYab8orshgs01yWqTTbvKM+Z2S0SL1yLRfVgb7hj54Os043n5E28Yc+9Fw8jztDvudbC+vzK0OtnLTn7ro2WQ44ZvtFxmUnmfzEXFUhusjbT85qa8xGtVHWm4+0Xjskt1q7LfaXpL9uHlY9T/6iLgzozWZt0Xgkdl8yn5f8WaskaMvOagIsSoic/I4vdZYhEbSJzqze+zH6bsbxB79c+N7EkdMNDJTtTFui5zFWURlsiMcTGLnMRF13pkzR0RsTbDYdSyMslf/HDpnDlQO6kxajnAwjxO1d07NWFF6nTq/LHbbLSqDHVGDSbVW5Fnf29+JN5JSvNleDY3dkCA/Pkf1e5YaJCJT3US07jfbQsNJdvNmsqUZjPN8qpUix6ydycvqz/j1/cc37UczPiXv5D7KKrtZ96E0v60p/ZMymHXRx/dvtYUGqr7WjhFVn2syGMURP8khRQxr5NhNRmAo51qnQ68LWotRLHGwcWO0PtVSmYtrufHfwlvnlY03e1n3JcUSB4uqvbjxTuc2fT8dby3Ws+WIaM1g4/unEn08vLkO1XDC8fB5YjPYnysUHqEiQcYFR9QC7djcvczeVpIu2Rtyp2wUSkfrBRF6wSHNPX1BeuGIE0VE6+gbN61O3O3h7PsmiCNRf7/qhpGyQ6TsWQZDvu80CwIRe0tzq3hE1HmeGOfL2miahYk65iAbZcfVfabsyG9rIDJQfaxX9M+zuAab3Qp6aq/2XsZmQ42JjCP1Z18f9cma74wM2dTG1/ajQWsxSZ/tGSwqc0lnb49uqA7Uc9F1ST9uxnxncrNlZ11waNeR23+azNVIyWCcZ6MZy5K5xq9FLpDFuXqQzE09T/VXzJdjlezx+Om13zjuDGo8zS1i31+ewWZnWi79UkhFd4SekhxEn4wovOMqm1uTzCwTNW4/tvWy6qoMhkQC69n6lKvi5/m6mJERmNqIu+qwbBkR9vPYRrtvKVIcbDQ++n0EzaJRMiJ0tyJFeGq+1PzH9zSyfdrzUBE7U14fNFbZb6YLun8pXA6G1g5ZmUtTu1jH1R4rqHGoeUu3pdQ40tHQUrtK+qJ/F2V/qeZB+giWdaT2pzaTLYv6kbXX88TUIhpZs3fG28Mx8iNnd0mfrPkiOmXaWjr2ovaz1uvoO55aLPSIaMlgmkjeWF3o//z9338k0G7Nepnc8XA2T2/Naa3ltOP3SOvllT86F2q/LNAMNj7fs/QGKiJzPc/a7IXoQemDRj5k/rPjITp/KgjMno+29fi+1m7UfGe2mz1DvePNXI2QDCZF5ozaC9WH60fK4YyNBBPtYnHyEbtKNtDaayZvtq7tNED9nTYYI2urXX/rPrbKc6FZjN7wfX/89H+/bCLDnDhd+2c0rSSLk0m9H2UTztYWedLaZdoN2UvS/rLIHTkyg1kjjvV9LdqjFRqRJfv1sqX3ETuj6+CtLcc/UxdBo91Qe2XWZNZ9TBHiYG3D9S1nFOr5KPlcfzXUfDWbZqa/ZTxOH6ovod38WrtFzC/K0bT7mULlYFLEGduVtReaCaP7XHZBM9Ksj8wXHU8jl5I/G8dzEYDYzaq3B3Rfj88vATFWa0fjzj7Ue6uR9I9quT9HtuN8pLlFziNrXpxMzb5C7IUS8pMcqKdrFtmix6r30HEtEbiP/Fw2s4yvqd2keVkypmQjdF6IfG5cFOs+lnA5mLb2Gt+zQo2piVTNMFm1GjdftBbKGF/TUvKoIOCp5aLn55HHyffUXg3IwbhMo/V4bjwLXsNSxwJOP62+GntRbfb41syplYeOFzW/KCIzGeRgSETReHpUxGky+o9lnJl+VLaMGJ9qtZsR0Xcc35o5NfPxbHrNfFo7yvToIK2P1FKYNqTmeLGamZNx0bV/D+n3746yvZtL2igRG2d2DOT+HDUH9JlomZbx0LKHw/R7Eb1n+kwkebNIOHuOkkUdGaIyNDWO52jcZ3yvHpp3kT2QUUtpsZ7IJKCfSBj7WU6UbWAqiravo8aNzlgSuwJV9JpyY2XNK0N/JJNRQSJsQ3ucL3ujSjK1UMeQLP29R7UIuZljrbCb5T3tMVBCNUBGBttxjJxlrvYcZeRZfUQ959GP+rpmfEl/Sa5382vez7abdoyI2qvh9lCv062OzJ73NUW0R5Z2U6LjaS+AtHJmYyFk242TGelUPdCLWRcaUgbIQDOP2fx2ZN5iHVFOp/o+GNV6b1lGxhs5tB3fp/qUnpTeXFu8E+2+1uwH1U9yUG0fyblNr8WaWSL63Dwqe70XaV9Ta61Ze3MG82Yu6XjoPcZp2lEe1S/eCXIy678+vofwxcE4T0U9PCJzcXK0/cjMV7wT7b62ZLIvDsZ56oraayZH2/dkLCmDleO9B2/thex38YiYlcGo4+HP3/Q/etuRsaIzc3Em6H7pn9fKEB0M8XAq0lszmSeDZdZoxbtA93PEvhZ/iHXszzwchctglrHQMbm+JvPV8fC9aIKtJviSGUyqxbyeTm10Tr6mja7V6qLjfSD7J6r2aizPYBnZyyIHjVgrdC3Wk5WxRuAMlll7cczGj8hoaPA4wblurwmz9wsnD8lY0bVX48uL2bVXU/akmmaW2bjnineQncng74MhZ9SZcO0m9WQwtJUyG6rnTv2rzW+59UMQX7jh9tDLmFGfh/+9HTv0u53ZmkfvidmJRJOxltKUltrZp39uyyQmzHS2fsYxWr/afW2/5tReiEK8RczOYKezUl9vpK9+XOaKzGTiLSJSs/TtW/j13fb7Cfv3qb7GrtWP6c+ek9YrAtLBpPRKZTJ0I0ZGhgx6x/JkLu4YItmx2tx2tDu1Ltz6LUFyOu1nufIglrnM5lkttolXjb8a8vtgaEQo9OyO5NXSx8fn+f8Ja+xbgF8up5vjWczincD/Hkyqvcq5/oWyi6UWeFs72mfWzx5/JeoIWhmMx3IsKd7N0lvEtyPZSXMCqP7afiaVwQKojFVwiBls7FcGo9Fm+hNqg2INIf8ebGw/BW7+lH0oe43jFO8D/r2ImpriU9Bkrqq9zuuvwBw5Uad7E/V9rkKLagMgzvRW5+IopyskoN9N37DWGrdvKqTWkmrTcZzic1DfIo4tclt2e0ZD5l23hkUKM6f6lLYoKKAjC1dLaC46bqvNOP0jfkq7KNTsziC7M9dNwaM4BE0tNmvb59a+pp3ZryjcRDrnzpabT1Gk8xYnKicsrgU9Nu1uUX2LIp1bnKacsiiKopB5a0ZD51cURVHchjbSn5rZoudTFEVRFEVRFEVRFEVRFK/iH96DRmHGTLfrAAAAAElFTkSuQmCC";
        stop1.setAttribute("stop-color", "#1B2023");
        stop2.setAttribute("stop-color", "#788578");
        stop2.setAttribute("stop-opacity", "1");
      }
    },
  },
  mounted() {
    // this.updateGradientColors();
  },
};
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.5s ease, transform 0.7s ease;
}

.fade-slide-enter,
.fade-slide-leave-to {
  transform: translateY(-100%);
}
.fade-slide-enter-from {
  opacity: 0;
  transition: opacity 1s ease-out, transform 0.5s ease;
}

.start {
  cursor: pointer;
}
.gradient-stop {
  transition: stop-color 0.5s ease, stop-opacity 0.5s ease;
}
.LogIn-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: auto;
  z-index: 5;
}
.menu-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: auto;
  z-index: 5;
}

/* 過渡效果 */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.75s ease;
}
.slide-enter {
  transform: translateY(-100%);
  opacity: 1;
}
.slide-leave-to {
  transform: translateY(-100%);
  /* opacity: 0; */
}
.slide-enter-from {
  transform: translateY(-100%);
  /* opacity: 0; */
}

.logo {
  width: 18.5rem;
  height: 100%;
  background-color: #75fb9f;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.mr-3 {
  margin-right: 1rem;
}

.full {
  height: 100vh; /* 讓整個視窗高度填充 */
  display: flex;
  flex-direction: column;
  background-color: #75fb9f;
}
.mid-container {
  flex-grow: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
}
.btnGroup {
  height: 100%;
  /* padding-right: 30px; */
}
.menu-btn {
  height: 100%;
  width: 4rem;
  background-color: #0038ff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.menu {
  margin-top: 1.5rem;
}
.sun-moon {
  margin-top: 1.5rem;
}
@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/Minecraft.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

h3 {
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 1.5rem;
  user-select: none;
  color: #1b2023;
}
p {
  margin: 0;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 2rem;
  user-select: none;
}
.startImage {
  pointer-events: none;
  user-select: none;
}
.rec1 {
  position: absolute;
  width: 30px;
  height: 30px;
  left: 3.5rem;
  top: 5.8rem;

  background: #1c1f1c;
}
.rec2 {
  /* Rectangle 3426 */

  position: absolute;
  width: 30px;
  height: 30px;
  left: 74.75rem;
  top: 36.5rem;

  background: #1c1f1c;
}

.rec3 {
  /* Rectangle 3427 */

  position: absolute;
  width: 30px;
  height: 30px;
  left: 72.875rem;
  top: 38.375rem;

  background: #1c1f1c;
}
.text1 {
  position: absolute;
  width: 12rem;
  height: 16.1875rem;
  left: 6.5625rem;
  top: 6.3rem;

  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 1.5rem;
  line-height: 1.4rem;
}

.text2 {
  position: absolute;
  width: 518px;
  height: 81px;
  left: 44.0625rem;
  top: 33.61rem;

  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 1.5rem;
  line-height: 1.4rem;
  /* or 96% */
}

/* 可根据需要添加自定义样式 */
.header {
  height: 7.1815rem; /* 让 header 高度占满整个视窗 */
  width: 100%;
}

.start-btn {
  width: 829px;
  height: 381px;
  margin-top: 4.5rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

/* Light-Mode */
.light-mode {
  transition: ease-out 0.3s;
}

/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}

.dark-mode p {
  color: #0fff50;
  transition: ease-out 0.35s;
}
.dark-mode svg rect {
  /* fill: #0fff50; */
  transition: ease-out 0.35s;
}
.dark-mode svg text {
  fill: black;
  transition: ease-out 0.35s;
}
svg text {
  margin: 0;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 1.5rem;
  fill: white;
  user-select: none;
}
</style>
