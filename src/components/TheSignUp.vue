<template>
  <div
    :class="{
      'dark-mode': isDarkMode,
    }"
    class="menu-container"
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
        <el-form class="form" :model="ruleForm" :rules="rules" ref="ruleForm">
          <div>
            <label for="email">Email</label>
            <el-input
              class="custom-el-input input"
              type="text"
              id="email"
              v-model="ruleForm.uname"
            />
          </div>
          <div>
            <label for="password">Password</label>
            <el-input
              class="custom-el-input input"
              type="password"
              id="password"
              v-model="ruleForm.password"
              autocomplete="off"
            />
          </div>
          <div class="remember-me">
            <el-checkbox class="custom-checkbox" v-model="checked">
            </el-checkbox>
            <label> Remember Me</label>
          </div>
          <div class="button-container">
            <el-button
              class="sign-in"
              type="primary"
              @click="submitForm('ruleForm')"
              >Sign in</el-button
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
</template>
<script>
import Cookies from "js-cookie";
import { ref } from "vue";
export default {
  mounted() {
    const rememberUser = Cookies.get("user");
    if (rememberUser) {
      this.ruleForm.uname = rememberUser;
    }
  },
  data() {
    return {
      ruleForm: {
        uname: "",
        password: "",
      },
      rules: {
        uname: [
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
    closeLogIn() {
      this.$emit("close-logIn");
    },
    submitForm(formName) {
      console.log(this.ruleForm.uname);
      // 验证表单中的账号密码是否有效，因为在上面rules中定义为了必填 required: true
      this.$refs[formName].validate((valid) => {
        // 点击登录后，让登录按钮开始转圈圈（展示加载动画）
        // this.loading = true;
        // 如果经过校验，账号密码都不为空，则发送请求到后端登录接口
        if (valid) {
          let _this = this;
          // 使用 axios 将登录信息发送到后端
          this.$axios({
            url: "/api/user/login", // 请求地址
            method: "post", // 请求方法
            headers: {
              // 请求头
              "Content-Type": "application/json",
            },
            params: {
              // 请求参数
              uname: _this.ruleForm.uname,
              password: _this.ruleForm.password,
            },
          }).then((res) => {
            // 当收到后端的响应时执行该括号内的代码，res 为响应信息，也就是后端返回的信息
            if (res.data.code === "0") {
              // 当响应的编码为 0 时，说明登录成功
              // 将用户信息存储到sessionStorage中
              sessionStorage.setItem("userInfo", JSON.stringify(res.data.data));
              // 跳转页面到首页
              this.$router.push("/profile");
              // 显示后端响应的成功信息
              this.$message({
                message: res.data.msg,
                type: "success",
              });
            } else {
              // 当响应的编码不为 0 时，说明登录失败
              // 显示后端响应的失败信息
              this.$message({
                message: res.data.msg,
                type: "warning",
              });
            }
            // 不管响应成功还是失败，收到后端响应的消息后就不再让登录按钮显示加载动画了
            // _this.loading = false;
            console.log(res);
          });
        } else {
          // 如果账号或密码有一个没填，就直接提示必填，不向后端请求
          console.log("error submit!!");
          // this.loading = false;
          return false;
        }
      });
    },
    login() {
      if (this.checked) {
        Cookies.set("user", this.ruleForm.uname, { expires: 100 });
      }
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
}
.title {
  padding: 3.5rem;
}
.form {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem; /* 控制表单项之间的间距 */
}

/* .form div {
  display: flex;
  flex-direction: column;
} */

label {
  margin-bottom: 8px; /* 标签与输入框之间的距离 */
  font-size: 1.25rem;
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 1.25rem;
  user-select: none;
  color: #000000;
}
.remember-me {
  display: flex;
  align-items: flex-end;
  gap: 0.8rem;
  position: relative;
  flex-direction: row;
}

.checkbox {
  box-sizing: border-box;
  width: 30px;
  height: 30px;
  background: #ffffff;
  border: 1px solid #000000;
  cursor: pointer;
  /* 移除 absolute 定位，这样 checkbox 会根据 flexbox 排列 */
}

.custom-el-input >>> .el-input__inner {
  box-sizing: border-box;
  width: 575px;
  height: 73px;
  padding: 10px; /* 调整内边距 */
  font-size: 1.5rem; /* 调整文字大小 */
  background: #ffffff;
  border: 1px solid #000000;
  cursor: pointer;
}
form div {
  display: block;
  margin-bottom: 1rem; /* 添加一些间距使其更易读 */
}

form label,
form .input {
  display: block;
  width: 100%; /* 使输入框占满容器宽度 */
  margin-top: 0.5rem; /* 添加一些顶部间距 */
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
  flex-grow: 1; /* 登陆功能占用剩余空间 */
  display: flex;
  flex-direction: column; /* 设置子项垂直排列 */
  padding: 2rem;
  align-items: center;
  justify-content: flex-start; /* 子项在上方开始 */
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

/* 样式设置 */
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
  background: #42e45d; /* 选中的背景颜色 */
  border: 1px solid #000000;
}

:deep(
    .custom-checkbox .el-checkbox__input.is-checked .el-checkbox__inner::after
  ) {
  width: 6px; /* 自定义勾选图标宽度 */
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

/* 悬停状态 */
.custom-checkbox .el-checkbox__inner:hover {
  border: 1px solid #00bfff; /* 悬停状态的边框颜色 */
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
</style>
