<template>
  <Transition name="fade-slide">
    <router-view />
  </Transition>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.5s ease, transform 1s ease;
}

.fade-slide-enter,
.fade-slide-leave-to {
  transform: translateY(-100%);
}
.fade-slide-enter-from {
  opacity: 0;
  transition: opacity 1s ease-out, transform 1s ease;
}
</style>
