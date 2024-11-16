<template>
  <div class="menu-container">
    <div class="main-content">
      <div class="logo">
        <svg
          width="207"
          height="165"
          viewBox="0 0 207 165"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <rect x="-8" width="215" height="164.932" fill="white" />
          <path
            d="M27.3424 81.1473V110.579C36.1338 110.961 48.1894 110.767 57.1566 107.904C66.5366 104.907 77.0327 98.73 82.384 92.6143V110.579C92.322 110.579 100.349 111.344 114.492 107.139C123.451 104.475 132.074 98.3478 138.19 92.6143V110.579H167.24V55.9199C157.302 56.3022 155.731 55.8014 146.599 57.4489C123.283 60.8889 121.414 74.1333 112.198 75.796V56.3022C112.198 56.3022 90.0286 55.1555 77.7972 61.6534C62.504 69.7797 54.8632 83.8229 27.3424 81.1473Z"
            fill="#13C9A8"
          />
          <path
            d="M50.9041 66.2671C43.0502 68.4348 41.2909 70.1941 39.1232 78.048C36.9556 70.1941 35.1963 68.4348 27.3424 66.2671C35.1963 64.0995 36.9556 62.3402 39.1232 54.4863C41.2909 62.3402 43.0502 64.0995 50.9041 66.2671Z"
            fill="#13C9A8"
          />
        </svg>
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

.logo {
  width: 18.5rem;
  height: 100%;
  /* background-color: #75fb9f; */
  /* align-items: center; */
  display: flex;
  flex-direction: column;
  flex: 3;

  /* justify-content: center; */
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
