<template>
  <div class="container-fluid min-vh-100 d-flex flex-column">
    <!-- Header 部分 -->
    <header
      class="d-flex justify-content-end p-3 position-relative"
      style="top: 1rem"
    >
      <div class="d-flex">
        <div class="mr-5"><the-menu-btn></the-menu-btn></div>
        <div class="mr-5"><the-sun-moon-btn></the-sun-moon-btn></div>
      </div>
    </header>

    <!-- 中间内容部分 -->
    <div class="d-flex position-relative vw-100">
      <div class="position-absolute create-position">
        <h1 class="display-1">CREATES</h1>
        <!-- <p class="lead">This is a sample content</p> -->
      </div>
      <div class="position-absolute arrow-position svg-container">
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
      </div>
      <the-new-era class="era-position"></the-new-era>
      <div class="position-absolute investment-position">
        <p class="lead">of</p>
        <h1 class="display-1">{ INVESTMENT }</h1>
      </div>
      <div class="square-position">
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
          <rect x="196.923" y="200" width="98.4615" height="100" fill="black" />
          <rect x="295.385" y="200" width="98.4615" height="100" fill="black" />
          <rect x="393.846" y="100" width="98.4615" height="100" fill="black" />
          <rect x="590.769" width="98.4615" height="100" fill="black" />
          <rect x="787.692" y="100" width="98.4615" height="100" fill="black" />
          <rect x="984.615" y="100" width="98.4615" height="100" fill="black" />
          <rect x="1181.54" y="100" width="98.4615" height="100" fill="black" />
          <rect x="787.692" y="200" width="98.4615" height="100" fill="black" />
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
      </div>
    </div>
  </div>
</template>

<script>
import TheMenuBtn from "./accessories/TheMenuBtn.vue";
import TheSunMoonBtn from "./accessories/TheSunMoonBtn.vue";
import TheNewEra from "./accessories/TheNewEra.vue";
export default {
  components: {
    TheMenuBtn,
    TheSunMoonBtn,
    TheNewEra,
  },
};
</script>

<style scoped>
@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/MinecraftRegular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

/* 可根据需要添加自定义样式 */
header {
  width: 100%;
}

h1 {
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: clamp(2rem, 6vw, 6vw);
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
  left: 10%;
  top: 9vh;
}

.arrow-position {
  left: 45%;
  top: 19.5vh;
}

.era-position {
  position: absolute;
  left: 73%;
  top: 19vh;
  transform: translateX(-50%);
}
.investment-position {
  left: 10%;
  top: 35vh;
}

.square-position {
  width: 100%;
  height: 20vh;
  position: absolute; /* 使其固定在页面底部 */
  top: 60vh;
  left: 0;
  right: 0;
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
}
</style>
