<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <div class="header">
      <div class="back-btn">
        <svg
          @click="navigateTo('/main')"
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M26.6667 3.3335V5.00016H23.3333V8.3335H20V11.6668H16.6667V15.0002H13.3333V16.6668H11.6667V18.3335H10V21.6668H11.6667V23.3335H13.3333V25.0002H16.6667V28.3335H20V31.6668H21.6667H23.3333V33.3335V35.0002H26.6667V36.6668H30V31.6668H26.6667V28.3335H23.3333V25.0002H20V21.6668H16.6667V18.3335H20V15.0002H23.3333V11.6668H26.6667V8.3335H30V3.3335H26.6667Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
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
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
          <path
            d="M10.1053 5.05263C6.73684 5.98232 5.98232 6.73684 5.05263 10.1053C4.12295 6.73684 3.36842 5.98232 0 5.05263C3.36842 4.12295 4.12295 3.36842 5.05263 0C5.98232 3.36842 6.73684 4.12295 10.1053 5.05263Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
        </svg>
      </div>
    </div>
    <div class="logout-div">
      <a href="#" class="logout-link" @click="logout">Log out</a>
    </div>
    <div class="main-content">
      <div class="left-content">
        <div class="user-profile">
          <div class="user-photo">
            <div class="monster-photo">
              <img class="monster-img" :src="currentMonsterUrl" />
            </div>
            <div class="edit-div"></div>
            <div class="level-div">
              <svg
                width="45"
                height="57"
                viewBox="0 0 45 57"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M0 15.7588L22.5 0L45 15.7588V41.2412L22.5 57L0 41.2412V15.7588Z"
                  fill="url(#paint0_linear_909_315)"
                />
                <defs>
                  <linearGradient
                    id="paint0_linear_909_315"
                    x1="22.5"
                    y1="0"
                    x2="22.5"
                    y2="57"
                    gradientUnits="userSpaceOnUse"
                  >
                    <stop offset="0.3" stop-color="#F2A9CF" />
                    <stop offset="1" stop-color="#FF9E1F" />
                  </linearGradient>
                </defs>
              </svg>
            </div>
          </div>
          <div class="user-Info-div">
            <div class="user-name-field">
              <h1>JAMES</h1>

              <svg
                width="20"
                height="20"
                viewBox="0 0 20 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M10 16.667H17.5"
                  stroke="black"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M13.75 2.9162C14.0815 2.58468 14.5312 2.39844 15 2.39844C15.2321 2.39844 15.462 2.44416 15.6765 2.533C15.891 2.62184 16.0858 2.75205 16.25 2.9162C16.4142 3.08036 16.5444 3.27523 16.6332 3.48971C16.722 3.70418 16.7678 3.93406 16.7678 4.1662C16.7678 4.39835 16.722 4.62822 16.6332 4.8427C16.5444 5.05718 16.4142 5.25205 16.25 5.4162L5.83333 15.8329L2.5 16.6662L3.33333 13.3329L13.75 2.9162Z"
                  stroke="black"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </div>
            <div class="share-div">
              <div class="share-btn">
                <text>91_1223</text>
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 20 20"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M3.33333 10V16.6667C3.33333 17.1087 3.50893 17.5326 3.82149 17.8452C4.13405 18.1577 4.55797 18.3333 5 18.3333H15C15.442 18.3333 15.866 18.1577 16.1785 17.8452C16.4911 17.5326 16.6667 17.1087 16.6667 16.6667V10"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M13.3333 5.00033L10 1.66699L6.66667 5.00033"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M10 1.66699V12.5003"
                    stroke="black"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </div>
            </div>
            <div class="exp-div">
              <h3>level 3</h3>
              <div class="exp-bar"></div>
            </div>
          </div>
        </div>
        <div class="left-middle-div">
          <div class="streak-div">
            <img :src="require('/src/images/target.png')" />
            <div class="middle">
              <h2>3</h2>
              <h3>Day Streak</h3>
            </div>
          </div>
          <div class="gem-div">
            <img :src="require('/src/images/gem.png')" />
            <div class="middle">
              <h2>X6</h2>
              <h3>Gems</h3>
            </div>
          </div>
          <div class="monster-div">
            <img :src="require('/src/images/bottle.png')" />
            <div class="middle">
              <h2>4</h2>
              <h3>Monsters</h3>
            </div>
          </div>
        </div>
        <div class="left-bottom-div">
          <h2>Account details</h2>
          <div class="email-div">
            <div class="email-text">
              <h3>Email</h3>
              <h3>Edit</h3>
            </div>
            <input class="custom-input input" type="email" id="login-email" />
          </div>
          <div class="password-div">
            <div class="password-text">
              <h3>Password</h3>
              <h3>Edit</h3>
            </div>
            <input
              class="custom-input input"
              type="password"
              id="login-password"
              autocomplete="off"
            />
          </div>
        </div>
      </div>
      <div class="right-content">
        <div class="top-container">
          <div class="collection-div"></div>
          <div class="favorite-div"></div>
        </div>
        <div class="bottom"></div>
      </div>
    </div>
  </div>
</template>

<!-- script  -->
<script>
export default {
  data() {
    return {
      monsters: [
        {
          id: "1",
          name: "monster1",
          url: "/images/monster1.png",
        },
        {
          id: "2",
          name: "monster2",
          url: "/images/monster2.png",
        },
        {
          id: "3",
          name: "monster3",
          url: "/images/monster3.png",
        },
        {
          id: "4",
          name: "monster4",
          url: "/images/monster4.png",
        },
      ],
      currentMonster: "1",
      isDarkMode: false,
    };
  },
  components: {},
  mounted() {
    const storedDarkMode = sessionStorage.getItem("isDarkMode");
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
  computed: {
    currentMonsterUrl() {
      // 隨機生成 1 到 4 之間的數字
      const randomNum = Math.floor(Math.random() * 4) + 1;
      // 使用 find 方法根據 ID 查找對應怪物
      const selectedMonster = this.monsters.find(
        (monster) => monster.id === randomNum.toString()
      );
      console.log(
        selectedMonster ? selectedMonster.url : "未找到對應的怪物圖片"
      );
      // 回傳對應 URL，若無匹配則回傳空字串或預設圖片 URL
      return selectedMonster ? selectedMonster.url : "";
    },
  },

  methods: {
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.$router.push(path);
    },
    logout() {
      console.log(sessionStorage.getItem("access"));
      this.$axios({
        url: "http://127.0.0.1:8000/login/logout/", // 確保這裡的 URL 正確
        method: "post",
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem("access")}`, // 添加 access token
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          // 登出成功，處理成功回應
          this.$message({
            message: "登出成功！",
            type: "success",
            duration: 3000,
          });
          // 清除存儲的 token
          sessionStorage.removeItem("access");
          sessionStorage.removeItem("refresh");
          // 導向登錄頁面或主頁
          this.$router.push("/home"); // 重定向到首頁
        })
        .catch((error) => {
          // 登出失敗，處理錯誤回應
          const message =
            error.response?.data?.detail || "登出失敗，請稍後再試。";
          this.$message({
            message: message,
            type: "error",
          });
        })
        .finally(() => {
          // 無論成功或失敗，都應確保 token 被清除，並重定向到登錄頁面
          sessionStorage.removeItem("access");
          sessionStorage.removeItem("refresh");
          this.$router.push("/home"); // 強制回到登錄頁面
        });
    },
  },
};
</script>

<!-- style  -->
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

/* logout btn  */
.logout-div {
  justify-content: flex-end;
  align-items: center;
  height: 5vh;
  width: 100%;
  display: flex;
}
.logout-link {
  padding-right: 0.5rem;
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

/* main content  */
.main-content {
  display: flex;
  flex: 1;
  flex-direction: row;
  padding-top: 2.5rem;
  padding-bottom: 3.5rem;
}
.left-content,
.right-content {
  flex-direction: column;
  display: flex;
  width: 50%;
}
.left-content {
  padding-left: 5.7rem;
  padding-right: 29px;
}
.right-content {
  padding-right: 1rem;
  padding-left: 2rem;
}

.user-profile {
  display: flex;
}
.user-photo {
  position: relative;
  width: 205px;
  height: 261px;
  background-color: #1b2023;
  border-radius: 50%;
}
.monster-photo {
  position: relative;
  width: 100%; /* 確保填滿父容器 */
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
}
.monster-img {
  position: absolute;
  margin-top: 20px;
}
.edit-div {
  position: absolute;
  margin-left: 12px;
  bottom: 0;
  width: 66px;
  height: 23px;
  border-radius: 10px;
  background-color: #d9d9d9;
  display: flex;
  justify-content: center;
  align-items: center;
}
.level-div {
  margin-bottom: 4px;
  margin-right: 30px;
  position: absolute;
  bottom: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.user-Info-div {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding-left: 1.5rem;
}
.user-name-field {
  width: 100%;
  flex: 1;
  display: flex;
  align-items: flex-end;
}
.user-name-field h1 {
  height: 60px; /* 假設 h1 的高度為 60px */
  line-height: 87px;
  vertical-align: bottom;
  font-family: "Micro5", sans-serif;
  /* font-weight: 300; */
  font-style: normal;
  font-size: 96px;
  user-select: none;
}

.share-div {
  flex: 0.4;
}

.share-btn {
  margin-top: 0.8rem;
  width: 135px;
  height: 26px;
  border-radius: 10px;
  background-color: #d9d9d9;
  display: flex;
  /* justify-content: center; */
  align-items: center;
}
.share-btn text {
  margin-left: 10px;
  margin-top: none;
}
.exp-div {
  flex: 0.6;
}
.exp-div h3 {
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 12px;
  user-select: none;
}
.exp-bar {
  width: 287px;
  height: 26px;
  background-color: #d9d9d9;
  border: 1px solid #000000;
}

.left-middle-div {
  display: flex;
  height: 80px;
  width: 100%;
  margin-top: 10px;
}
.streak-div {
  flex: 0.7;
  display: flex;
  align-items: center;
}
.gem-div,
.monster-div {
  flex: 0.5;
  display: flex;
  align-items: center;
}
.middle {
  margin-top: 0.25rem;
  padding-left: 0.5rem;
}
.middle h2 {
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 18px;
  user-select: none;
  margin: 0;
}
.middle h3 {
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 12px;
  user-select: none;
  color: #a7a9ac;
  margin-top: 3px;
  margin-bottom: 0;
}

.left-bottom-div {
  flex: 1;
  margin-top: 30px;
}
.left-bottom-div h2 {
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 16px;
  user-select: none;
  margin: 0;
}
.left-bottom-div h3 {
  font-family: "PressStar2PFont", sans-serif;
  font-style: normal;
  font-size: 12px;
  color: #a7a9ac;
  user-select: none;
  margin: 0;
}
.email-text,
.password-text {
  display: flex;
  justify-content: space-between;
  margin-top: 25px;
}

.custom-input {
  box-sizing: border-box;
  width: 100%;
  height: 49px;
  padding: 10px;
  font-size: 1.5rem;
  background-color: #00000000;
  border: 1px solid #000000;
  cursor: pointer;
}

.input-sys {
  flex-direction: column;
  width: 100%;
  /* padding: 2rem; */
  display: flex;

  justify-content: center;
  align-items: center;
}

.top-container {
  display: flex;
  flex: 1;
}

.collection-div,
.favorite-div {
  flex: 1;
  background-color: #d9d9d9;
  border-radius: 60px;
  margin-right: 1.2rem;
  margin-bottom: 1.5rem;
}
.bottom {
  flex: 1;
  background-color: #d9d9d9;
  border-radius: 60px;
  margin-right: 1.2rem;
  margin-bottom: 1.5rem;
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
</style>
<style>
input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px rgba(255, 255, 255, 0) inset !important; /* 設置背景顏色 */
  -webkit-text-fill-color: black !important; /* 設置文字顏色 */
}

.input .input__inner {
  all: unset;
}
</style>
