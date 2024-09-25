<template>
  <div class="newEra-size">
    <div class="d-flex newEra-button">
      <h1
        :class="{
          'dark-mode': isDarkMode,
          'light-mode': !isDarkMode,
        }"
        class="newEra-word"
      >
        NEW ERA
      </h1>
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
  color: #000000;
}
.light-mode {
  color: white;
}
.newEra-button {
  width: 100%;
  height: 100%;
  background: var(--neon-green, #75fb9f);
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 11px 11px 0 rgba(0, 0, 0, 1);
  pointer-events: none;
  cursor: pointer;
}

.newEra-word {
  width: 100%;
  font-family: "MinecraftFont", sans-serif;
  font-size: 10rem;
  font-style: normal;
  font-weight: 500;
  line-height: 0; /* 確保行高不影響垂直居中 */
  text-align: center;
  margin-top: 0.75rem;
  margin-left: 0.35rem;
  user-select: none;
  pointer-events: none;
}

.newEra-size {
  width: 34vw;
  height: 9vw;
  transform: translateX(-50%);
  cursor: pointer;
}

@media (max-width: 1950px) {
  .newEra-word {
    font-size: 7rem;
  }
  .newEra-button {
    box-shadow: 7.5px 7.5px 0 rgba(0, 0, 0, 1);
  }
}
@media (max-width: 1750px) {
  .newEra-word {
    font-size: 5.3rem;
  }
}
@media (max-width: 1120px) {
  .newEra-word {
    font-size: 4.5rem;
  }
  .newEra-button {
    box-shadow: 5px 5px 0 rgba(0, 0, 0, 1);
  }
}

@media (max-width: 789px) {
  .newEra-word {
    font-size: 2.5rem;
  }
  .newEra-button {
    box-shadow: 4px 4px 0 rgba(0, 0, 0, 1);
  }
}

@media (max-width: 639px) {
  .newEra-word {
    font-size: 2rem;
  }
  .newEra-button {
    box-shadow: 3px 3px 0 rgba(0, 0, 0, 1);
  }
}

@media (max-width: 490px) {
  .newEra-word {
    font-size: 1.3rem;
  }
}

@media (max-width: 350px) {
  .newEra-word {
    font-size: 1rem;
  }
}
</style>
