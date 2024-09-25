<template>
  <div class="light-mode full">
    <div
      class="header d-flex justify-content-between align-items-center position-relative"
    ></div>
    <div :class="{ 'dark-mode': isDarkMode }" class="main-content">
      <!-- <svg
        width="1209"
        height="634"
        viewBox="0 0 1209 634"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="83.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="8.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="83.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="483.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="283.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="683.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="183.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="583.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="383.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="783.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="883.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="983.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="133.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="58.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="533.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="333.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="733.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="233.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="633.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="433.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="833.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="933.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1033.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1108.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1158.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="108.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="33.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="508.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="308.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="708.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="208.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="608.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="408.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="808.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="908.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1008.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1083.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="158.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="558.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="358.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="758.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="258.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="658.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="23.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="458.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="3.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="43.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="283.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="163.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="403.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="63.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="303.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="183.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="423.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="83.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="323.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="203.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="443.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="103.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="343.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="223.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="463.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="523.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="583.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="123.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="363.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="243.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="483.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="543.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="603.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="143.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="383.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="263.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="858.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="958.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1058.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="503.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="563.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1133.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1183.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <circle cx="1205.5" cy="623.5" r="3.5" fill="#1C1F1C" />
        <path
          d="M0 631.5V619H2.5V616.5H5V614H12.5V616.5H15V619H17.5V631.5H12.5V626.5H5V631.5H0ZM5 624H12.5V619H10V616.5H7.5V619H5V624ZM27.3 631.5V629H32.3V616.5H29.8V614H37.3V629H42.3V631.5H27.3ZM52.1 631.5V629H57.1V616.5H54.6V614H62.1V629H67.1V631.5H52.1Z"
          fill="#1C1F1C"
        />
        <path
          d="M107.5 621.5H110V624H107.5V631.5H102.5V619H107.5V621.5ZM117.5 619V621.5H110V619H117.5ZM132.3 616.5V614H137.3V616.5H132.3ZM127.3 631.5V629H132.3V621.5H129.8V619H137.3V629H142.3V631.5H127.3ZM152.1 634V631.5H162.1V629H152.1V626.5H149.6V621.5H152.1V619H167.1V631.5H164.6V634H152.1ZM154.6 626.5H162.1V621.5H154.6V626.5ZM174.4 631.5V614H179.4V619H189.4V621.5H191.9V631.5H186.9V621.5H179.4V631.5H174.4ZM206.7 631.5V621.5H201.7V619H206.7V614H211.7V619H216.7V621.5H211.7V631.5H206.7ZM224 631.5V629H236.5V626.5H226.5V624H224V621.5H226.5V619H239V621.5H229V624H239V626.5H241.5V629H239V631.5H224Z"
          fill="#1C1F1C"
        />
        <path
          d="M282.5 621.5H285V624H282.5V631.5H277.5V619H282.5V621.5ZM292.5 619V621.5H285V619H292.5ZM302.3 631.5V629H299.8V621.5H302.3V619H314.8V621.5H317.3V626.5H304.8V629H314.8V631.5H302.3ZM304.8 624H312.3V621.5H304.8V624ZM324.6 631.5V629H337.1V626.5H327.1V624H324.6V621.5H327.1V619H339.6V621.5H329.6V624H339.6V626.5H342.1V629H339.6V631.5H324.6ZM351.9 631.5V629H349.4V621.5H351.9V619H364.4V621.5H366.9V626.5H354.4V629H364.4V631.5H351.9ZM354.4 624H361.9V621.5H354.4V624ZM381.7 621.5H384.2V624H381.7V631.5H376.7V619H381.7V621.5ZM391.7 619V621.5H384.2V619H391.7ZM406.5 631.5V629H404V626.5H401.5V619H406.5V626.5H411.5V619H416.5V626.5H414V629H411.5V631.5H406.5ZM426.3 631.5V629H423.8V621.5H426.3V619H438.8V621.5H441.3V626.5H428.8V629H438.8V631.5H426.3ZM428.8 624H436.3V621.5H428.8V624ZM451.1 631.5V629H448.6V621.5H451.1V619H461.1V614H466.1V631.5H451.1ZM453.6 629H461.1V621.5H453.6V629Z"
          fill="#1C1F1C"
        />
        <path
          d="M552 631.5V614H557V616.5H559.5V619H562V616.5H564.5V614H569.5V631.5H564.5V621.5H562V626.5H559.5V621.5H557V631.5H552ZM579.3 631.5V629H576.8V621.5H579.3V619H591.8V621.5H594.3V629H591.8V631.5H579.3ZM581.8 629H589.3V621.5H581.8V629ZM601.6 631.5V619H616.6V621.5H619.1V631.5H614.1V621.5H606.6V631.5H601.6ZM628.9 631.5V629H626.4V621.5H628.9V619H641.4V621.5H643.9V626.5H631.4V629H641.4V631.5H628.9ZM631.4 624H638.9V621.5H631.4V624ZM653.7 634V631.5H663.7V629H653.7V626.5H651.2V619H656.2V626.5H663.7V619H668.7V631.5H666.2V634H653.7Z"
          fill="#1C1F1C"
        />
        <path
          d="M703.5 631.5V629H701V626.5H706V629H713.5V614H718.5V629H716V631.5H703.5ZM725.8 631.5V619H728.3V616.5H730.8V614H738.3V616.5H740.8V619H743.3V631.5H738.3V626.5H730.8V631.5H725.8ZM730.8 624H738.3V619H735.8V616.5H733.3V619H730.8V624ZM750.6 631.5V614H755.6V616.5H758.1V619H760.6V616.5H763.1V614H768.1V631.5H763.1V621.5H760.6V626.5H758.1V621.5H755.6V631.5H750.6Z"
          fill="#1C1F1C"
        />
        <path
          d="M800 631.5V626.5H802.5V624H805V621.5H810V619H812.5V616.5H805V619H800V616.5H802.5V614H815V616.5H817.5V621.5H815V624H812.5V626.5H807.5V629H817.5V631.5H800ZM829.8 631.5V629H827.3V626.5H824.8V619H827.3V616.5H829.8V614H837.3V616.5H839.8V619H842.3V626.5H839.8V629H837.3V631.5H829.8ZM832.3 629H837.3V619H834.8V616.5H829.8V626.5H832.3V629ZM849.6 631.5V626.5H852.1V624H854.6V621.5H859.6V619H862.1V616.5H854.6V619H849.6V616.5H852.1V614H864.6V616.5H867.1V621.5H864.6V624H862.1V626.5H857.1V629H867.1V631.5H849.6ZM884.4 631.5V626.5H874.4V621.5H876.9V619H879.4V616.5H881.9V614H889.4V624H891.9V626.5H889.4V631.5H884.4ZM879.4 624H884.4V619H881.9V621.5H879.4V624Z"
          fill="#1C1F1C"
        />
        <rect
          x="505.333"
          y="621"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="507.5"
          y="621"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="509.667"
          y="621"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="511.833"
          y="623.166"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="511.833"
          y="625.334"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="511.833"
          y="627.5"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="511.833"
          y="629.666"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="509.667"
          y="631.834"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="507.5"
          y="631.834"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="505.333"
          y="631.834"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="503.167"
          y="631.834"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="501"
          y="629.666"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="501"
          y="627.5"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="501"
          y="625.334"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="501"
          y="623.166"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="503.167"
          y="621"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="508.258"
          y="623.709"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="506.092"
          y="623.709"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="503.925"
          y="625.875"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="503.925"
          y="628.041"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="506.092"
          y="629.125"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
        <rect
          x="508.258"
          y="629.125"
          width="2.16667"
          height="2.16667"
          fill="#1C1F1C"
        />
      </svg> -->
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isDarkMode: false,
    };
  },
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
  methods: {
    closeMenu() {
      this.$emit("close-menu");
    },
  },
};
</script>
<style scoped>
@font-face {
  font-family: "MinecraftFont";
  src: url("../assets/fonts/Minecraft.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
.full {
  height: 100vh; /* 讓整個視窗高度填充 */
  display: flex;
  flex-direction: column;
}
.header {
  height: 6.25rem; /* 让 header 高度占满整个视窗 */
  width: 100%;
  background-color: #75fb9f;
}

.main-content {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}
</style>
