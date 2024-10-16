<template>
  <div class="align-justify">
    <div class="menu-button">
      <div
        class="vector"
        :class="{
          'dark-mode': !isDarkMode,
          'light-mode': isDarkMode,
        }"
      ></div>
      <div
        class="vector"
        :class="{
          'dark-mode': !isDarkMode,
          'light-mode': isDarkMode,
        }"
      ></div>
      <div
        class="vector"
        :class="{
          'dark-mode': !isDarkMode,
          'light-mode': isDarkMode,
        }"
      ></div>
      <div
        class="vector"
        :class="{
          'dark-mode': !isDarkMode,
          'light-mode': isDarkMode,
        }"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isDarkMode: {
      type: Boolean,
      required: true,
    },
  },
};
</script>

<style scoped>
.dark-mode {
  background-color: #000000;
}
.light-mode {
  background-color: white;
}
/* align-justify */
.align-justify {
  width: clamp(2rem, 2.68rem, 5rem); /* 最小值3rem，理想值5vw，最大值5rem */
  height: clamp(
    1.6rem,
    1.6rem,
    1.6rem
  ); /* 最小值1.6rem，理想值2.6vw，最大值2.6rem */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* menu-button */
.menu-button {
  width: clamp(
    1.5rem,
    2.3rem,
    2.2rem
  ); /* 最小值1.5rem，理想值2.2vw，最大值2.2rem */
  height: clamp(
    1rem,
    1.65rem,
    1.75rem
  ); /* 最小值1rem，理想值1.5vw，最大值1.5rem */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.3s ease;
  cursor: pointer;
}

.menu-button:hover {
  transform: scale(1.1); /* 當懸停時放大 */
}

/* Vector Base Style */
.vector {
  width: 100%;
  height: 3px;

  border-radius: 1.5px; /* 3px 的一半 */
}
</style>
