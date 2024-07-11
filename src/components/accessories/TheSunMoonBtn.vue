<template>
  <div class="container">
    <div class="sun">
      <div
        class="vector"
        v-for="(vector, index) in vectors"
        :key="index"
        :style="vector.style"
      ></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      vectors: [
        {
          style: {
            left: "34.87%",
            right: "23.46%",
            top: "31.46%",
            bottom: "26.88%",
          },
        },
        {
          style: {
            left: "57.68%",
            right: "42.32%",
            top: "8.25%",
            bottom: "83.42%",
          },
        },
        {
          style: {
            left: "50.86%",
            right: "49.14%",
            top: "91.3%",
            bottom: "0.36%",
          },
        },
        {
          style: {
            left: "24.28%",
            right: "69.81%",
            top: "18.96%",
            bottom: "75.12%",
          },
        },
        {
          style: {
            left: "78.17%",
            right: "15.91%",
            top: "82.51%",
            bottom: "11.57%",
          },
        },
        {
          style: {
            left: "8.25%",
            right: "83.42%",
            top: "50.17%",
            bottom: "49.83%",
          },
        },
        { style: { left: "91.3%", right: "0.36%", top: "57%", bottom: "43%" } },
        {
          style: {
            left: "19.45%",
            right: "74.63%",
            top: "77.68%",
            bottom: "16.4%",
          },
        },
        {
          style: {
            left: "82.99%",
            right: "11.09%",
            top: "23.79%",
            bottom: "70.29%",
          },
        },
      ],
    };
  },
};
</script>

<style scoped>
.container {
  position: relative;
  width: 100%;
  height: 100%;
}

.sun {
  position: relative;
  width: 18px;
  height: 18px;
  left: 38.23px;
  top: 16.69px;
  transform: rotate(4.7deg);
}

.vector {
  position: absolute;
  border: 2px solid #000000;
  transform: rotate(4.7deg);
  border-radius: 1.39px;
}
</style>
