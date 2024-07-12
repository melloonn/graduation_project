<template>
  <div class="wrap-check-64">
    <label class="switch" for="checkbox">
      <input type="checkbox" id="checkbox" />
      <div class="slider round"></div>
      <svg
        class="moon"
        xmlns="http://www.w3.org/2000/svg"
        width="21"
        height="20"
        viewBox="0 0 21 20"
        fill="none"
      >
        <g clip-path="url(#clip0_229_67)">
          <path
            d="M17.2329 11.066C17.0107 12.3287 16.4335 13.502 15.5688 14.4486C14.7042 15.3953 13.5878 16.0761 12.3503 16.4114C11.1128 16.7467 9.80548 16.7226 8.58118 16.342C7.35688 15.9614 6.2663 15.24 5.43704 14.2622C4.60778 13.2844 4.07415 12.0906 3.89858 10.8206C3.72301 9.55061 3.91277 8.25686 4.44565 7.09076C4.97853 5.92465 5.8325 4.93443 6.90762 4.23595C7.98274 3.53747 9.23456 3.15963 10.5166 3.14664C9.68881 4.0932 9.22828 5.30544 9.21875 6.56286C9.20921 7.82027 9.65131 9.03935 10.4646 9.99836C11.278 10.9574 12.4085 11.5926 13.6506 11.7885C14.8927 11.9845 16.1638 11.7281 17.2329 11.066Z"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </g>
        <defs>
          <clipPath id="clip0_229_67">
            <rect
              width="18"
              height="18"
              fill="white"
              transform="translate(2.32166 0.215332) rotate(4.6992)"
            />
          </clipPath>
        </defs>
      </svg>
      <svg
        class="sun"
        xmlns="http://www.w3.org/2000/svg"
        width="21"
        height="21"
        viewBox="0 0 21 21"
        fill="none"
      >
        <g clip-path="url(#clip0_229_57)">
          <path
            d="M10.1559 14.1336C12.22 14.3032 14.0309 12.7675 14.2005 10.7034C14.3702 8.63929 12.8345 6.82845 10.7704 6.65878C8.70625 6.48911 6.89541 8.02485 6.72574 10.089C6.55607 12.1531 8.09181 13.9639 10.1559 14.1336Z"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M11.139 2.17383L11.0162 3.66879"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M9.91016 17.1235L9.78727 18.6185"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M5.12579 4.10254L6.09996 5.25121"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M14.8263 15.541L15.8005 16.6897"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M2.24084 9.72021L3.7358 9.8431"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M17.1904 10.9492L18.6854 11.0721"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M4.16971 15.7333L5.31838 14.7591"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M15.6079 6.03261L16.7565 5.05844"
            stroke="black"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </g>
        <defs>
          <clipPath id="clip0_229_57">
            <rect
              width="18"
              height="18"
              fill="white"
              transform="translate(2.23071 0.688965) rotate(4.6992)"
            />
          </clipPath>
        </defs>
      </svg>
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
.moon {
  cursor: pointer;
  position: relative;
  top: 9px;
  left: 7px;
}
.sun {
  cursor: pointer;
  top: -7.5px;
  left: 26.5px;
  position: absolute;
}
.wrap-check-64 .switch {
  display: inline-block;
  height: 26px;
  position: relative;
  width: 54px;
}

.wrap-check-64 .switch input {
  display: none;
}

.wrap-check-64 .slider {
  background-color: #a7a9ac;
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
  background-color: #75fb9f;
  /* bottom: 2px; */
  content: "";
  height: 26px;
  /* left: 7px; */
  position: absolute;
  transition: 0.4s;
  width: 26px;
}

.wrap-check-64 input:checked + .slider {
  background-color: #fff;
}

.wrap-check-64 input:checked + .slider:before {
  transform: translateX(28px);
}

.wrap-check-64 .slider.round {
  border-radius: 34px;
}

.wrap-check-64 .slider.round:before {
  border-radius: 50%;
}
</style>
