<template>
  <div class="align-justify">
    <div class="menu-button">
      <div class="vector"></div>
      <div class="vector"></div>
      <div class="vector"></div>
      <div class="vector"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AlignJustify",
};
</script>

<style scoped>
/* align-justify */
.align-justify {
  width: 2.6875rem; /* 43px */
  height: 2.6875rem; /* 43px */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* menu-button */
.menu-button {
  width: 2.015625rem; /* 32.25px */
  height: 1.34375rem; /* 21.5px */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.3s ease; /* 添加過渡效果 */
}

.menu-button:hover {
  transform: scale(1.1); /* 當懸停時放大 */
}

/* Vector Base Style */
.vector {
  width: 100%;
  height: 3px;
  background-color: #000000;
  border-radius: 1.5px; /* 3px 的一半 */
}
</style>
