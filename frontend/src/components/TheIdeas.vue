<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }"></div>
</template>
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
  methods: {},
};
</script>

<style scoped>
.full {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #75fb9f;
}

/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}
</style>
