<template>
  <div class="wrap-check-64">
    <label class="switch" for="checkbox">
      <input type="checkbox" id="checkbox" />
      <div class="slider round"></div>
    </label>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style scoped>
.wrap-check-64 .switch {
  display: inline-block;
  height: 34px;
  position: relative;
  width: 60px;
}

.wrap-check-64 .switch input {
  display: none;
}

.wrap-check-64 .slider {
  background-color: #ccc;
  bottom: 0;
  cursor: pointer;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  transition: 0.4s;
  transform: rotate(135deg);
}

.wrap-check-64 .slider:before {
  background-color: #fff;
  bottom: 4px;
  content: "";
  height: 26px;
  left: 4px;
  position: absolute;
  transition: 0.4s;
  width: 26px;
}

.wrap-check-64 input:checked + .slider {
  background-color: #66bb6a;
}

.wrap-check-64 input:checked + .slider:before {
  transform: translateX(26px);
}

.wrap-check-64 .slider.round {
  border-radius: 34px;
}

.wrap-check-64 .slider.round:before {
  border-radius: 50%;
}
</style>
