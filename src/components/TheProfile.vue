<template>
  <div class="container-fluid min-vh-100 d-flex flex-column">
    <!-- Header 部分 -->
    <header class="d-flex justify-content-end p-3 position-relative">
      <div class="ml-auto d-flex">
        <the-menu-btn class="mr-2"></the-menu-btn>
        <the-sun-moon-btn></the-sun-moon-btn>
      </div>
    </header>

    <!-- 中间内容部分 -->
    <div class="flex-grow-1 d-flex align-items-center justify-content-center">
      <div class="text-center">
        <h1 class="display-4">Welcome to My Homepage</h1>
        <p class="lead">This is a sample content</p>
        <!-- 其他内容 -->
      </div>
    </div>
  </div>
</template>

<script>
import TheMenuBtn from "./accessories/TheMenuBtn.vue";
import TheSunMoonBtn from "./accessories/TheSunMoonBtn.vue";

export default {
  components: {
    TheMenuBtn,
    TheSunMoonBtn,
  },
};
</script>

<style scoped>
/* 可根据需要添加自定义样式 */
header {
  width: 100%;
}
</style>
