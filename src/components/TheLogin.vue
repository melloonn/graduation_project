<template>
  <div class="login-page">
    <el-card class="box-card">
      <h2>Login</h2>
      <el-form
        :model="ruleForm"
        status-icon
        :rules="rules"
        ref="ruleForm"
        label-position="left"
        label-width="70px"
        class="login-from"
      >
        <el-form-item label="帳號" prop="uname">
          <el-input v-model="ruleForm.uname"></el-input>
        </el-form-item>
        <el-form-item label="密碼" prop="password">
          <el-input
            type="password"
            v-model="ruleForm.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div class="btnGroup">
        <el-checkbox v-model="checked" label="記住帳密" size="large" />
        <el-button type="primary" @click="submitForm('ruleForm')"
          >Login</el-button
        >
        <el-button @click="resetForm('ruleForm')">Reset</el-button>
        <router-link to="/register">
          <el-button style="margin-left: 10px">Register</el-button>
        </router-link>
      </div>
    </el-card>
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
    submitForm(formName) {
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
              this.$router.push("/home");
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
    resetForm(formName) {
      this.$refs[formName].resetFields();
      Cookies.remove("user");
    },
    login() {
      if (this.checked) {
        Cookies.set("user", this.ruleForm.uname, { expires: 100 });
      }
    },
  },
};
</script>

<style scoped>
.login-page {
  padding: 2rem;
  display: flex;
  flex-direction: column; /* 垂直布局 */
  align-items: center; /* 水平居中对齐 */
  justify-content: center; /* 垂直居中对齐 */
}
.box-card {
  margin: auto auto;
  width: 400px;
}
.login-from {
  margin: auto auto;
}
</style>
