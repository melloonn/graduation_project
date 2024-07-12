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
  width: clamp(3rem, 5vw, 5rem); /* 最小值3rem，理想值5vw，最大值5rem */
  height: clamp(
    1.6rem,
    2.6vw,
    2.6rem
  ); /* 最小值1.6rem，理想值2.6vw，最大值2.6rem */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* menu-button */
.menu-button {
  width: clamp(
    1.5rem,
    2.2vw,
    2.2rem
  ); /* 最小值1.5rem，理想值2.2vw，最大值2.2rem */
  height: clamp(
    1rem,
    1.5vw,
    1.5rem
  ); /* 最小值1rem，理想值1.5vw，最大值1.5rem */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.3s ease;
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
