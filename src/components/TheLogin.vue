<template>
  <div>
    <!-- Sign in -->
    <div
      :class="{
        'dark-mode': isDarkMode,
      }"
      class="menu-container"
      v-show="!isSignupOpen"
    >
      <svg
        width="185"
        height="832"
        viewBox="0 0 185 832"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect width="92" height="92" fill="white" />
        <rect x="92" y="92" width="93" height="93" fill="#A7A9AC" />
        <rect x="92" y="277" width="93" height="93" fill="black" />
        <rect y="185" width="92" height="92" fill="#A7A9AC" />
        <rect y="277" width="92" height="93" fill="#A7A9AC" />
        <rect x="92" y="370" width="93" height="92" fill="#A7A9AC" />
        <rect y="462" width="92" height="93" fill="black" />
        <rect x="92" y="647" width="93" height="93" fill="#A7A9AC" />
        <rect y="740" width="92" height="92" fill="#A7A9AC" />
        <rect y="555" width="92" height="92" fill="black" />
        <rect x="92" y="92" width="19" height="19" fill="white" />
        <rect x="92" y="129" width="19" height="19" fill="white" />
        <rect x="92" y="166" width="19" height="19" fill="white" />
        <rect x="129" y="92" width="19" height="19" fill="white" />
        <rect x="129" y="129" width="19" height="19" fill="white" />
        <rect x="129" y="166" width="19" height="19" fill="white" />
        <rect x="111" y="111" width="18" height="18" fill="white" />
        <rect x="111" y="148" width="18" height="18" fill="white" />
        <rect x="166" y="92" width="19" height="19" fill="white" />
        <rect x="166" y="129" width="19" height="19" fill="white" />
        <rect x="166" y="166" width="19" height="19" fill="white" />
        <rect x="148" y="111" width="18" height="18" fill="white" />
        <rect x="148" y="148" width="18" height="18" fill="white" />
      </svg>
      <div class="login-box">
        <div class="back" @click="closeLogIn">
          <svg
            class="back-btn"
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
        <div class="input-sys">
          <div class="title">
            <h1>Welcome!</h1>
          </div>
          <el-form
            class="form"
            :model="loginForm"
            :rules="rules"
            ref="loginForm"
          >
            <div class="email-div">
              <label for="login-email">Email</label>
              <div class="field-group">
                <el-input
                  class="custom-el-input input"
                  type="text"
                  id="login-email"
                  v-model="loginForm.email"
                />
                <svg
                  class="svg-btn"
                  width="40"
                  height="40"
                  viewBox="0 0 40 40"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M35 6.66667V5H4.99998V6.66667H3.33331V33.3333H4.99998V35H35V33.3333H36.6666V6.66667H35ZM33.3333 11.6667H31.6666V13.3333H28.3333V15H25V16.6667H21.6666V18.3333H18.3333V16.6667H15V15H11.6666V13.3333H8.33331V11.6667H6.66665V10H8.33331V8.33333H31.6666V10H33.3333V11.6667ZM33.3333 30H31.6666V31.6667H8.33331V30H6.66665V16.6667H8.33331V18.3333H11.6666V20H15V21.6667H16.6666V23.3333H23.3333V21.6667H25V20H28.3333V18.3333H31.6666V16.6667H33.3333V30Z"
                    fill="#A7A9AC"
                  />
                </svg>
              </div>
            </div>
            <div class="password-div">
              <label for="login-password">Password</label>
              <div class="field-group">
                <el-input
                  class="custom-el-input input"
                  :type="isPasswordVisible ? 'text' : 'password'"
                  id="login-password"
                  v-model="loginForm.password"
                  autocomplete="off"
                />
                <svg
                  @click="togglePasswordVisibility"
                  class="svg-btn"
                  width="40"
                  height="40"
                  viewBox="0 0 40 40"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M23.3333 15H16.6667V16.6667H15V23.3333H16.6667V25H23.3333V23.3333H25V16.6667H23.3333V15ZM21.6667 21.6667H18.3333V18.3333H21.6667V21.6667Z"
                    fill="#A7A9AC"
                  />
                  <path
                    d="M35 15V11.6667H33.3334V10H31.6667V8.33333H28.3334V5H11.6667V8.33333H8.33335V10H6.66669V11.6667H5.00002V15H1.66669V25H5.00002V28.3333H6.66669V30H8.33335V31.6667H11.6667V35H28.3334V31.6667H31.6667V30H33.3334V28.3333H35V25H38.3334V15H35ZM35 21.6667H31.6667V25H30V26.6667H28.3334V28.3333H25V31.6667H15V28.3333H11.6667V26.6667H10V25H8.33335V21.6667H5.00002V18.3333H8.33335V16.6667V15H10V13.3333H11.6667V11.6667H15V8.33333H25V11.6667H28.3334V13.3333H30V15H31.6667V18.3333H35V21.6667Z"
                    fill="#A7A9AC"
                  />
                </svg>
              </div>
            </div>
            <div class="remember-me">
              <div class="remember-div">
                <el-checkbox class="custom-checkbox" v-model="checked">
                </el-checkbox>
                <label class="remember"> Remember Me</label>
              </div>
              <a href="#" class="forgot-link">forget password?</a>
            </div>
            <div class="button-container">
              <el-button
                class="sign-in"
                type="primary"
                @click="submitForm('loginForm')"
                >Sign in</el-button
              >
            </div>
            <div class="signup-div">
              <label> New User?</label>
              <a
                href="#"
                class="signup-link"
                @click="
                  {
                    closeLogIn();
                    openSignUp();
                  }
                "
                >Sign up</a
              >
            </div>
          </el-form>
        </div>
      </div>
      <svg
        width="185"
        height="832"
        viewBox="0 0 185 832"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect x="93" width="92" height="92" fill="#A7A9AC" />
        <rect x="93" y="92" width="92" height="93" fill="black" />
        <rect y="185" width="93" height="92" fill="#A7A9AC" />
        <rect x="93" y="277" width="92" height="93" fill="white" />
        <rect y="370" width="93" height="92" fill="#A7A9AC" />
        <rect y="462" width="93" height="93" fill="black" />
        <rect x="93" y="462" width="92" height="93" fill="black" />
        <rect x="93" y="555" width="92" height="92" fill="#A7A9AC" />
        <rect y="647" width="93" height="93" fill="black" />
        <rect x="93" y="740" width="92" height="92" fill="#A7A9AC" />
        <rect y="462" width="19" height="19" fill="white" />
        <rect y="499" width="19" height="19" fill="white" />
        <rect y="536" width="19" height="19" fill="white" />
        <rect x="19" y="481" width="18" height="18" fill="white" />
        <rect x="19" y="518" width="18" height="18" fill="white" />
        <rect x="56" y="481" width="18" height="18" fill="white" />
        <rect x="56" y="518" width="18" height="18" fill="white" />
        <rect x="93" y="481" width="18" height="18" fill="white" />
        <rect x="93" y="518" width="18" height="18" fill="white" />
        <rect x="130" y="481" width="18" height="18" fill="white" />
        <rect x="130" y="518" width="18" height="18" fill="white" />
        <rect x="167" y="481" width="18" height="18" fill="white" />
        <rect x="167" y="518" width="18" height="18" fill="white" />
        <rect x="37" y="462" width="19" height="19" fill="white" />
        <rect x="37" y="499" width="19" height="19" fill="white" />
        <rect x="37" y="536" width="19" height="19" fill="white" />
        <rect x="74" y="462" width="19" height="19" fill="white" />
        <rect x="74" y="499" width="19" height="19" fill="white" />
        <rect x="74" y="536" width="19" height="19" fill="white" />
        <rect x="111" y="462" width="19" height="19" fill="white" />
        <rect x="111" y="499" width="19" height="19" fill="white" />
        <rect x="111" y="536" width="19" height="19" fill="white" />
        <rect x="148" y="462" width="19" height="19" fill="white" />
        <rect x="148" y="499" width="19" height="19" fill="white" />
        <rect x="148" y="536" width="19" height="19" fill="white" />
      </svg>
    </div>
    <!-- Sign up -->
    <!-- <div class="sign-up-page">
      <Transition>
        <the-register
          v-show="isSignupOpen"
          :is-dark-mode="isDarkMode"
          @close-signup="toggleSignup"
        ></the-register>
      </Transition>
    </div> -->
  </div>
</template>
<script>
import TheRegister from "./TheRegister.vue";
import Cookies from "js-cookie";
import { ref } from "vue";
export default {
  mounted() {
    const rememberUser = Cookies.get("user");
    if (rememberUser) {
      this.loginForm.email = rememberUser;
    }
  },
  components: {
    TheRegister,
  },
  data() {
    return {
      isPasswordVisible: false,
      isSignupOpen: false,
      loginForm: {
        email: "",
        password: "",
      },
      rules: {
        email: [
          {
            required: true,
            message: "Username can't be empty！",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message: "Password can't be empty！",
            trigger: "blur",
          },
        ],
      },
      checked: ref(false),
    };
  },
  methods: {
    toggleSignup() {
      this.isSignupOpen = !this.isSignupOpen;
    },
    closeLogIn() {
      this.$emit("close-logIn");
    },
    openSignUp() {
      this.$emit("open-sign-up");
    },
    togglePasswordVisibility() {
      this.isPasswordVisible = !this.isPasswordVisible;
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          let _this = this;

          // 這裡的請求 URL 要確保正確
          this.$axios({
            url: "http://127.0.0.1:8000/login/login/", // 修改為正確的 URL
            method: "post",
            headers: {
              "Content-Type": "application/json",
            },
            // 將 email 和 password 包裝到請求的 body 中
            data: {
              email: _this.loginForm.email,
              password: _this.loginForm.password, // 確保這裡有傳入密碼
            },
          })
            .then((res) => {
              // 登入成功
              this.$message({
                message: "登入成功！",
                type: "success",
                duration: 3000,
              });
              sessionStorage.setItem("access", res.data.access);
              sessionStorage.setItem("refresh", res.data.refresh);
              this.$router.push("/main");
            })
            .catch((error) => {
              // 登入失敗
              const message =
                error.response?.data?.detail ||
                "登入失敗，請檢查電子郵件和密碼。";
              this.$message({
                message: message,
                type: "error",
              });
              console.error("登入錯誤:", error);
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
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
<style scoped>
.button-container {
  display: flex;
  align-items: center;
  justify-content: center;
}
.sign-in {
  width: 19.5625rem;
  height: 4.5625rem;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 8px 8px 0 rgba(0, 0, 0, 1);
  cursor: pointer;
  background: #0fff50;
  border: none;
  font-size: 1.25rem;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 1.25rem;
  color: #000000;
  margin-bottom: 0.7rem;
}
.title {
  padding: 1.75rem;
}
.form {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.email-div {
  margin-bottom: 3rem;
  position: relative;
}
.password-div {
  margin-bottom: 1rem;
  position: relative;
}
.signup-div {
  display: flex;
  gap: 1rem;
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-end;
  margin-top: 1rem;
}
label {
  margin-bottom: 8px;
  font-size: 16px;
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  user-select: none;
  color: #a7a9ac;
}
a {
  margin-bottom: 8px;
  font-size: 16px;
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  user-select: none;
  color: #000000;
  text-decoration: none;
}
.remember-div {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.remember-me {
  margin-bottom: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.remember {
  /* margin-bottom: 8px; */
  margin-left: 1rem;
}

.checkbox {
  box-sizing: border-box;
  width: 30px;
  height: 30px;
  background: #ffffff;
  border: 1px solid #000000;
  cursor: pointer;
}

.custom-el-input >>> .el-input__inner {
  box-sizing: border-box;
  width: 35.94rem;
  height: 4.56rem;
  padding: 10px;
  font-size: 1.5rem;
  background-color: #ffffff;
  border: 1px solid #000000;
  cursor: pointer;
}
.field-group {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}
.svg-btn {
  position: absolute;
  margin-top: 7px;
  margin-right: 30px;
}
form div {
  display: block;
}

form label,
form .input {
  margin-top: 0.5rem;
}
.input-sys {
  flex-direction: column;
  width: 100%;
  /* padding: 2rem; */
  display: flex;

  justify-content: center;
  align-items: center;
}
.back-btn {
  display: flex;
  justify-content: center;
  align-items: center;
}
.back {
  align-self: flex-start;
  padding: 1rem;
  cursor: pointer;
}
.login-box {
  flex: 1;
  height: auto;
  display: flex;
  flex-direction: column;
  padding: 2rem;
  align-items: center;
  justify-content: flex-start;
  position: relative;
}
@font-face {
  font-family: "PressStar2PFont";
  src: url("../assets/fonts/PressStart2P-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

h1 {
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 3rem;
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

.custom-checkbox {
  box-sizing: border-box;
  width: 30px;
  height: 30px;
  background: #ffffff;
  border: 1px solid #000000;
  cursor: pointer;
}
:deep(.el-checkbox__inner) {
  width: 30px;
  height: 30px;
  border: 1px solid #000000;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* 选中状态 */
:deep(.custom-checkbox .el-checkbox__input.is-checked .el-checkbox__inner) {
  background: #42e45d;
  border: 1px solid #000000;
}

:deep(
    .custom-checkbox .el-checkbox__input.is-checked .el-checkbox__inner::after
  ) {
  width: 6px;
  height: 13px;
  border: 3px solid rgb(255, 255, 255);
  border-left: 0;
  border-top: 0;
  left: 9px;
  top: 5px;
}
:deep(.custom-checkbox .el-checkbox__input.is-checked + .el-checkbox__label),
:deep(.el-checkbox__label) {
  font-size: 16px;
  font-weight: 500;
}

.custom-checkbox .el-checkbox__inner:hover {
  border: 1px solid #00bfff;
}
</style>

<style>
.el-input .el-input__inner {
  all: unset;
}
.el-input__wrapper {
  all: unset;
}
.el-input__wrapper:hover {
  all: unset;
}
.el-form {
  all: unset;
}

.el-button {
  all: unset;
}

/* @media (max-width: 1600px) {
  html {
    font-size: 16px;
  }
}

@media (max-width: 1300px) {
  html {
    font-size: 13px;
  }
}

@media (max-width: 1000px) {
  html {
    font-size: 10px;
  }
} */
</style>
