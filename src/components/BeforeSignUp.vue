<template>
  <div
    :class="{
      'dark-mode': isDarkMode,
    }"
    class="menu-container"
  >
    <div class="left-content">
      <div class="back-btn">
        <svg
          @click="closeBefore"
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M26.6667 3.3335V5.00016H23.3333V8.3335H20V11.6668H16.6667V15.0002H13.3333V16.6668H11.6667V18.3335H10V21.6668H11.6667V23.3335H13.3333V25.0002H16.6667V28.3335H20V31.6668H21.6667H23.3333V33.3335V35.0002H26.6667V36.6668H30V31.6668H26.6667V28.3335H23.3333V25.0002H20V21.6668H16.6667V18.3335H20V15.0002H23.3333V11.6668H26.6667V8.3335H30V3.3335H26.6667Z"
            fill="white"
          />
        </svg>
      </div>
      <svg
        width="360"
        height="144"
        viewBox="0 0 360 144"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M0 68.2652V143.625C22.623 144.604 53.6459 144.105 76.7213 136.774C100.859 129.101 127.869 113.285 141.639 97.6262V143.625C167.213 143.625 187.869 145.583 224.262 134.817C247.318 127.995 269.508 112.307 285.246 97.6262V143.625H360V3.6709C334.426 4.6496 330.384 3.3675 306.885 7.5857C246.885 16.394 242.075 50.306 218.361 54.5634V4.6496C218.361 4.6496 161.311 1.7135 129.836 18.3514C90.482 39.1586 70.8197 75.1161 0 68.2652Z"
          fill="#75FB9F"
        />
        <path
          d="M60.6316 30.1646C40.4211 35.7149 35.8939 40.2195 30.3158 60.3292C24.7377 40.2195 20.2105 35.7149 0 30.1646C20.2105 24.6143 24.7377 20.1097 30.3158 0C35.8939 20.1097 40.4211 24.6143 60.6316 30.1646Z"
          fill="#75FB9F"
        />
      </svg>
    </div>
    <div class="right-content">
      <div class="title-div"><h1>Join Us!</h1></div>
      <div class="main-content">
        <GoogleLogin :callback="callback">
          <div class="google-div" tabindex="0">
            <img
              :src="require('/src/images/Google logo.png')"
              class="google-logo"
            />
            <text>login by <span class="highlight">Gmail</span></text>
          </div>
        </GoogleLogin>
        <div class="apple-div" tabindex="0">
          <img :src="require('/src/images/Apple.png')" class="apple-logo" />
          <text>login by <span class="highlight">Apple ID</span></text>
        </div>
        <div class="separator">
          <span>or</span>
        </div>
        <div class="createAccount-div" @click="toggleSignup" tabindex="0">
          <text>create account</text>
        </div>
        <div class="annotation">
          <p>By signing up, you agree to the Terms of Service</p>
          <p>and Privacy Policy, including Cookie Usage Policy.</p>
        </div>
        <div class="note">
          <text>Already have Account?</text>
        </div>
        <div class="Login-div" @click="toggleLogIn" tabindex="0">
          <text>Login</text>
        </div>
      </div>
    </div>
  </div>

  <!-- Login  -->
  <Transition name="slide">
    <div class="full" v-show="isLogInOpen">
      <the-login
        :is-dark-mode="isDarkMode"
        @close-logIn="toggleLogIn"
        @open-sign-up="openSignUp"
      ></the-login>
    </div>
  </Transition>

  <!-- Sign up -->
  <Transition name="slide">
    <div class="full" v-show="isSignupOpen">
      <the-register
        :is-dark-mode="isDarkMode"
        @close-signup="toggleSignup"
        @open-logIn="openLogin"
      ></the-register>
    </div>
  </Transition>
</template>

<script>
import Cookies from "js-cookie";
import { ref } from "vue";
import TheRegister from "./TheRegister.vue";
import TheLogin from "./TheLogin.vue";

export default {
  mounted() {
    window.handleCredentialResponse = this.handleCredentialResponse;
  },
  data() {
    return {
      isDarkMode: false, // 主頁面中的 darkMode 狀態
      isMenuOpen: false,
      isLogInOpen: false,
      isSignupOpen: false,
    };
  },
  components: {
    TheRegister,
    TheLogin,
  },
  methods: {
    toggleLogIn() {
      this.isLogInOpen = !this.isLogInOpen;
    },
    toggleSignup() {
      this.isSignupOpen = !this.isSignupOpen;
    },
    openSignUp() {
      this.isSignupOpen = true;
    },
    openLogin() {
      this.isLogInOpen = true;
    },
    closeBefore() {
      this.$emit("close-before");
    },
    handleCredentialResponse(response) {
      const token = response.credential;
      console.log(token);
      // 將 token 發送到後端進行驗證
      this.verifyToken(token);
    },
    verifyToken(token) {
      // 假設後端有一個 /auth/google 驗證路由
      this.$axios
        .post("/auth/google", { token })
        .then((response) => {
          console.log("登入成功", response.data);
          // 在此處進行登入成功後的處理
        })
        .catch((error) => {
          console.error("登入失敗", error);
        });
    },
    closeSignup() {
      this.$emit("close-signup");
    },
    closeLogin() {
      this.$emit("close-login");
    },
  },
  props: {
    isDarkMode: {
      type: Boolean,
      required: true,
    },
  },
};
</script>

<script setup>
const callback = (response) => {
  // This callback will be triggered when the user selects or login to
  // his Google account from the popup
  console.log("Handle the response", response);
};
</script>

<style scoped>
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

.full {
  left: 0;
  top: 0;
  position: absolute;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #75fb9f;
  z-index: 10;
}
/* left-content */
.left-content {
  flex: 1;
  background-color: #1b2023;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}
/* header */

.back-btn {
  margin: 20px;
  position: absolute;
  top: 0;
  left: 0;
  cursor: pointer;
}
.button-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* right-content */
.right-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title-div {
  margin-top: 8rem;
  margin-bottom: 5.5rem;
}
.google-div,
.apple-div {
  position: relative;
  height: 58px;
  width: 400px;
  background-color: white;
  border-radius: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.google-div {
  margin-bottom: 35px;
}
text {
  position: absolute;
  left: 0;
  margin-left: 92px;
  font-family: "PressStar2PFont", sans-serif;
  font-size: 16px;
  user-select: none;
}
.highlight {
  color: #13c9a8;
}
.google-logo,
.apple-logo {
  position: absolute;
  left: 0;
  margin-left: 42px;
  margin-bottom: 4px;
}

.separator {
  display: flex;
  align-items: center;
  text-align: center;
  width: 100%;
  margin: 20px 0;
  color: black; /* 字體顏色 */
}

.separator::before,
.separator::after {
  content: "";
  flex: 1;
  border-bottom: 1px solid black; /* 分隔線顏色 */
}

.separator::before {
  margin-right: 10px;
}

.separator::after {
  margin-left: 5px;
}

.separator span {
  /* padding: 0 5px; */
  font-size: 16px;
  user-select: none;
  font-family: "PressStar2PFont", sans-serif;
  color: black; /* or 字串顏色 */
}

.createAccount-div {
  position: relative;
  height: 58px;
  width: 400px;
  background-color: #21ab30;
  border-radius: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.createAccount-div text {
  position: relative;
  margin: 0;
  font-family: "PressStar2PFont", sans-serif;
  font-size: 16px;
  color: white;
  user-select: none;
}

.Login-div {
  position: relative;
  border: 2px solid #21ab30;
  height: 58px;
  width: 400px;
  background: none;
  border-radius: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.Login-div text {
  margin: 0;
  position: relative;
  font-family: "PressStar2PFont", sans-serif;
  font-size: 16px;
  color: #21ab30;
  user-select: none;
}

.annotation {
  margin-top: 0.75rem;
  margin-bottom: 1.5rem;
}
.note {
  height: 20px;
  width: 400px;
  margin-bottom: 0.75rem;
  padding-left: 1rem;
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: flex-start;
}
.note text {
  margin: 0;
  position: relative;
  font-family: "PressStar2PFont", sans-serif;
  font-size: 16px;
  user-select: none;
}

@font-face {
  font-family: "PressStar2PFont";
  src: url("../assets/fonts/PressStart2P-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
p {
  margin: 0;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 8px;
  user-select: none;
  color: #a7a9ac;
}
h1 {
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 50px;
  user-select: none;
  color: #1b2023;
}
.menu-container {
  width: 100vw;
  height: 100vh;
  flex-direction: row;
  margin: 0;
  padding: 0;
  display: flex;
  background-color: #75fb9f;
  justify-content: space-between;
}
.dark-mode {
  background-color: #1b2023;
}
.dark-mode form label {
  color: white;
}
.dark-mode h1 {
  color: white;
}
.dark-mode svg path {
  fill: white;
}
.dark-mode .sign-in {
  background-color: white;
}
.dark-mode a {
  color: #13c9a8;
}
</style>
