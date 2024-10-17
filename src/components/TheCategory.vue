<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <!-- header  -->
    <div class="header">
      <div class="back-btn">
        <svg
          @click="toggleExpandBack"
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
            :fill="isDarkMode ? 'black' : 'black'"
          />
          <path
            d="M10.1053 5.05263C6.73684 5.98232 5.98232 6.73684 5.05263 10.1053C4.12295 6.73684 3.36842 5.98232 0 5.05263C3.36842 4.12295 4.12295 3.36842 5.05263 0C5.98232 3.36842 6.73684 4.12295 10.1053 5.05263Z"
            :fill="isDarkMode ? 'black' : 'black'"
          />
        </svg>
      </div>
    </div>
    <!-- main div  -->
    <div class="main-content">
      <!-- select-div  -->
      <div class="selection-div">
        <!-- box1  -->
        <div class="box1">
          <Transition name="slideOrigin">
            <div v-if="!isExpend" class="originDiv1">
              <div class="blackbox1">
                <svg
                  width="60"
                  height="60"
                  viewBox="0 0 60 60"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  @click="toggleExpand"
                  v-if="!isExpend"
                  style="cursor: pointer"
                >
                  <path
                    d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
                    stroke="#75FB9F"
                    stroke-width="4"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M30 20V40"
                    stroke="#75FB9F"
                    stroke-width="4"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M20 30H40"
                    stroke="#75FB9F"
                    stroke-width="4"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </div>
              <div class="linearBox"></div>
              <div class="linearBox"></div>
              <div class="linearBox"></div>
            </div>
          </Transition>

          <Transition name="slide1">
            <div v-if="isExpend" class="animateDiv1">
              <div class="select-div"><h2>// SELECT</h2></div>
              <div class="types-div" tabindex="0">
                <p>Types</p>
              </div>
              <div
                class="names-div"
                :class="{ 'name-pressed': isNamesPress }"
                @click="toggleNames"
                tabindex="0"
              >
                <p>Names</p>
                <div :class="['namesArrow', { 'rotate-arrow': isNamesPress }]">
                  <svg
                    width="40"
                    height="39"
                    viewBox="0 0 40 39"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M8.33325 11.375H9.99992V13H11.6666V14.625H13.3333V16.25H14.9999V17.875H16.6666V19.5H18.3333V21.125H19.9999V22.75H21.6666V24.375H23.3333V26H24.9999V27.625H14.9999V30.875H31.6666V14.625H28.3333V24.375H26.6666V22.75H24.9999V21.125H23.3333V19.5H21.6666V17.875H19.9999V16.25H18.3333V14.625H16.6666V13H14.9999V11.375H13.3333V9.75H11.6666V8.125H8.33325V11.375Z"
                      :fill="isNamesPress ? '#75fb9f' : 'white'"
                    />
                  </svg>
                </div>
              </div>
            </div>
          </Transition>
        </div>
        <!-- box2  -->
        <div class="box2">
          <Transition name="slideOrigin">
            <div v-if="!isExpend" class="originDiv2">
              <div class="blackbox2"></div>
              <div class="linearBox"></div>
              <div class="linearBox"></div>
              <div class="linearBox"></div>
            </div>
          </Transition>

          <Transition name="slide2">
            <div v-if="isExpend" class="animateDiv2"></div>
          </Transition>
          <!-- enterprise-list  -->
          <Transition name="slideList">
            <div class="button-list" v-if="isNamesPress">
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
          </Transition>
        </div>
        <!-- box3  -->
        <div class="box3">
          <Transition name="slideOrigin">
            <div v-if="!isExpend" class="originDiv3">
              <div class="blackbox3"></div>
              <div class="linearBox"></div>
              <div class="linearBox"></div>
              <div class="linearBox"></div>
            </div>
          </Transition>

          <Transition name="slide3">
            <div v-if="isExpend" class="animateDiv3"></div>
          </Transition>
        </div>

        <!-- text  -->
        <Transition name="slideOrigin">
          <div class="text-div" v-if="!isExpend">
            <h1 class="rotated-text">ENTERPRISES</h1>
          </div>
        </Transition>
      </div>

      <!-- generator-div  -->
      <Transition name="slideGenerator">
        <div v-show="isExpend" class="generator-div">
          <div>
            <svg
              width="616"
              height="706"
              viewBox="0 0 616 706"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <rect x="438" width="178" height="129" rx="30" fill="#1C1F1C" />
              <path
                d="M0.5 70.1739C0.5 53.8815 13.7076 40.6738 30 40.6738H615.5V675.913C615.5 692.205 602.292 705.413 586 705.413H30C13.7076 705.413 0.5 692.205 0.5 675.913V70.1739Z"
                fill="#75FB9F"
                stroke="black"
              />
            </svg>
          </div>
        </div>
      </Transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDarkMode: false,
      isExpend: false,
      isNamesPress: false,
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
    handleClick(item) {
      console.log(`Clicked on: ${item.name}`);
      // Your custom function can be triggered here
    },
    toggleExpand() {
      this.isExpend = !this.isExpend; // 切換 expand 狀態
      this.isNamesPress = false;
    },
    toggleNames() {
      this.isNamesPress = !this.isNamesPress;
    },
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.$router.push(path);
    },
    toggleExpandBack() {
      if (this.isExpend) {
        this.isExpend = false;
        this.isNamesPress = false;
      } else {
        this.navigateTo("/enterprise_selection");
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

/* main content  */
.main-content {
  display: flex;
  flex: 1;
  flex-direction: row;
}

/* selection-div  */
.selection-div {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 45vw;
}
.generator-div {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 0.75rem;
  flex: 1;
}

.box1 {
  position: relative;
  display: flex;
  flex: 1;
  width: 32vw;
  overflow: hidden;
}
.box2 {
  position: relative;
  display: flex;
  flex: 1;
  width: 33.5vw;
}

.box3 {
  position: relative;
  display: flex;
  flex: 1;
  width: 35vw;
}

.animateDiv1 {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  background-color: #1b2023;
  width: 100%;
  height: 100%;
}
.select-div {
  height: 55%;
  width: 100%;
  align-items: center;
  padding-left: 1rem;
  display: flex;
}
.types-div {
  flex: 1;
  border-top: 1px solid white;
  border-bottom: 1px solid white;
  display: flex;
  align-items: center;
  padding-left: 2.25rem;
  color: white;
}
.names-div {
  position: relative;
  flex: 1;
  border-bottom: 1px solid white;
  display: flex;
  align-items: center;
  padding-left: 2.25rem;
  color: white;
}
.name-pressed {
  color: #75fb9f;
}
.namesArrow {
  position: absolute;
  right: 20px;
  margin-bottom: 2.5px;
  transition: transform 0.5s ease;
}
.rotate-arrow {
  transform: rotate(-90deg); /* 當 isNamePress 為 true 時旋轉 270 度 */
}

.animateDiv2 {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  background-color: #1b2023;
  width: 100%;
  height: 100%;
}
.animateDiv3 {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  background-color: #1b2023;
  width: 100%;
  height: 100%;
}

/* div1  */
.originDiv1 {
  display: flex;
  flex-direction: row;
  width: 100%;
  flex: 1;
  gap: 3vw;
}
.blackbox1 {
  display: flex;
  justify-content: center;
  padding-top: 3rem;
  padding-right: 1rem;
  width: 13vw;
  background-color: #1b2023;
}
.linearBox {
  background: linear-gradient(to right, #1b2023, #75fb9f);
  height: 100%;
  width: 3vw;
}
/* div2  */
.originDiv2 {
  display: flex;
  flex-direction: row;
  width: 100%;
  flex: 1;
  gap: 3vw;
}
.blackbox2 {
  display: flex;
  justify-content: center;
  width: 14.5vw;
  background-color: #1b2023;
}
/* div3  */
.originDiv3 {
  flex: 1;
  display: flex;
  width: 100%;
  flex-direction: row;
  gap: 3vw;
}
.blackbox3 {
  display: flex;
  justify-content: center;
  width: 16vw;
  background-color: #1b2023;
}

/* text-div  */
.text-div {
  position: absolute;
  display: inline-block;
  bottom: 9.5rem;
  left: -7.5rem;
}

/* enterprise-list  */
.button-list {
  position: absolute;
  width: 250px;
  height: 500px;
  overflow-y: auto;
  padding: 10px;
  box-sizing: border-box;
  top: 5px;
  left: 30px;
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

/* font  */
@font-face {
  font-family: "Micro5";
  src: url("../assets/fonts/Micro5-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/Minecraft.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "Inter";
  src: url("../assets/fonts/Inter.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
h1 {
  margin: 0;
  font-family: "Micro5", sans-serif;
  font-style: normal;
  font-size: 100px;
  user-select: none;
  color: #75fb9f;
  transform: rotate(270deg);
}
h2 {
  margin: 0;
  font-family: "Micro5", sans-serif;
  font-style: normal;
  font-size: 65px;
  user-select: none;
  color: #75fb9f;
}
p {
  margin: 0;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-size: 32px;
  user-select: none;
  /* color: white; */
}
.list-div {
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 200%;
  user-select: none;
  letter-spacing: 0.5em;
  color: white;
}
/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}
.dark-mode border {
  border: 2px solid #75fb9f;
}

/* animate  */
.slide1-enter-active,
.slide1-leave-active {
  transition: all 0.75s ease;
}
.slide1-enter {
  transform: translateX(-100%);
  opacity: 1;
}
.slide1-leave-to {
  transform: translateX(-100%);
}
.slide1-enter-from {
  transform: translateX(-100%);
}

.slide2-enter-active {
  transition: all 0.75s ease;
  transition-delay: 0.75s;
}
.slide2-leave-active {
  transition: all 0.75s ease;
}
.slide2-enter {
  transform: translateX(-100%);
  opacity: 1;
}
.slide2-leave-to {
  transform: translateX(-100%);
  /* opacity: 0; */
}
.slide2-enter-from {
  transform: translateX(-100%);
  /* opacity: 0; */
}

.slide3-enter-active {
  transition: all 0.75s ease;
  transition-delay: 1.5s;
}
.slide3-leave-active {
  transition: all 0.75s ease;
}
.slide3-enter {
  transform: translateX(-100%);
  opacity: 1;
}
.slide3-leave-to {
  transform: translateX(-100%);
  /* opacity: 0; */
}
.slide3-enter-from {
  transform: translateX(-100%);
  /* opacity: 0; */
}

.slideOrigin-enter-active {
  transition: transform 0.75s ease;
  transition-delay: 0.75s;
}
.slideOrigin-leave-active {
  transition: transform 0.75s ease;
}
.slideOrigin-enter {
  transform: translateX(-100%);
  opacity: 1;
}
.slideOrigin-leave-to {
  transform: translateX(-100%);
  /* opacity: 0; */
}
.slideOrigin-enter-from {
  transform: translateX(-100%);
  /* opacity: 0; */
}

.slideList-enter-active {
  transition: transform 0.75s ease;
}
.slideList-leave-active {
  transition: transform 0.75s ease;
}
.slideList-enter {
  transform: translateX(-100%);
  opacity: 1;
}
.slideList-leave-to {
  transform: translateX(-100%);
  /* opacity: 0; */
}
.slideList-enter-from {
  transform: translateX(-100%);
  /* opacity: 0; */
}

.slideGenerator-enter-active {
  transition: transform 0.75s ease;
  transition-delay: 1.5s;
}
.slideGenerator-leave-active {
  transition: transform 0.75s ease;
}
.slideGenerator-enter {
  transform: translateX(100%);
  opacity: 1;
}
.slideGenerator-leave-to {
  transform: translateX(100%);
  /* opacity: 0; */
}
.slideGenerator-enter-from {
  transform: translateX(100%);
  /* opacity: 0; */
}
</style>
