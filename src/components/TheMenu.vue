<template>
  <div class="menu-container">
    <div class="main-content">
      <div class="logo-container">
        <div class="logo">LOGO</div>
      </div>
      <div class="list-container">
        <div class="close" @click="closeMenu">Close</div>
        <ul>
          <li>About</li>
          <li>Service</li>
          <li>Projects</li>
        </ul>
      </div>
    </div>
    <div class="footer">
      <div class="footer-logo"><h1>@2024</h1></div>
      <div class="footer-li">
        <div class="footer-left">
          <div>FAQs</div>
          <div>Stock</div>
          <div>FAQs</div>
        </div>
        <div class="footer-right">
          <div>Contact</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    closeMenu() {
      this.$emit("close-menu");
    },
  },
};
</script>
<style scoped>
@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/Minecraft.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

h1 {
  margin: 0;
  display: inline-block;
  white-space: nowrap;
  font-family: "MinecraftFont", sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 7rem;
  user-select: none;
  color: #1b2023;
}
.menu-container {
  width: 100vw;
  height: 86vh;
  flex-direction: column;
  margin: 0;
  padding: 0;
  display: flex;
  background-color: #17b8a6;
}

.header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #17b8a6;
}

.logo-container {
  padding: 5rem 3.5rem;
  display: flex;
  flex: 3;
  /* align-items: center; */
}
.logo {
  color: var(--white, #fff);
  font-size: 36px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
}

.close {
  padding: 3rem 0rem 2.5rem 0rem;

  color: var(--white, #fff);
  font-size: 24px;
  font-style: normal;
  font-weight: 300;
  line-height: normal;
  cursor: pointer;
  user-select: none;
}

.list-container {
  display: flex;
  flex: 2;
  flex-direction: column;
  align-items: flex-start;
}
.main-content {
  height: 68.5vh;
  flex-grow: 1;
  background-color: #17b8a6;
  display: flex;
  justify-content: center;
  align-items: stretch;
}

.main-content ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  /* text-align: right; */
}

.main-content li {
  color: var(--white, #fff);

  font-size: 32px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
  margin-bottom: 0.75rem;
  user-select: none;
  cursor: pointer;
}

.footer {
  display: flex;
  height: 18vh;
  justify-content: space-between;
  background-color: white;
}
.footer-logo {
  /* padding: 5rem 3.5rem; */
  margin-left: 1.5rem;
  display: flex;
  align-items: center;
  flex: 3;
}
.footer-li {
  padding-top: 2rem;
  display: flex;
  flex-direction: row;
  flex: 2;
}

.footer-left,
.footer-right {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.footer-left div,
.footer-right div {
  font-size: 1rem;
  user-select: none;
}
</style>
