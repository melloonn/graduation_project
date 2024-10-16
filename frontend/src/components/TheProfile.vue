<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <div class="header">
      <div class="back-btn">
        <svg
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
    <div class="logout-div">
      <a href="#" class="logout-link">Log out</a>
    </div>
    <div class="main-content">
      <div class="left-content">
        <div class="user-profile">
          <div class="user-photo"></div>
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
      isDarkMode: false,
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
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.$router.push(path);
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
  padding-left: 5.5rem;
}
.right-content {
  padding-right: 1rem;
  padding-left: 2rem;
}

.user-profile {
  display: flex;
}
.user-photo {
  width: 205px;
  height: 261px;
  background-color: #1b2023;
  border-radius: 50%;
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
</style>
