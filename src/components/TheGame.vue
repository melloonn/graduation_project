<template>
  <div class="unity-container">
    <iframe
      src="/Unity/index.html"
      frameborder="0"
      width="100%"
      height="100%"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script>
export default {
  name: "UnityGame",
};
</script>

<style scoped>
.unity-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 充滿整個視窗的高度 */
  width: 100vw; /* 充滿整個視窗的寬度 */
}

iframe {
  border: none; /* 去掉邊框 */
  width: 100%; /* 讓iframe充滿容器 */
  height: 100%; /* 讓iframe充滿容器 */
}
</style>
