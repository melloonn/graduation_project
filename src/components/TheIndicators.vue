<template>
  <div class="full" :class="{ 'dark-mode': isDarkMode }">
    <!-- header  -->
    <div class="header">
      <div class="back-btn">
        <svg
          @click="navigateTo('/enterprise_selection')"
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M26.6667 3.3335V5.00016H23.3333V8.3335H20V11.6668H16.6667V15.0002H13.3333V16.6668H11.6667V18.3335H10V21.6668H11.6667V23.3335H13.3333V25.0002H16.6667V28.3335H20V31.6668H21.6667H23.3333V33.3335V35.0002H26.6667V36.6668H30V31.6668H26.6667V28.3335H23.3333V25.0002H20V21.6668H16.6667V18.3335H20V15.0002H23.3333V11.6668H26.6667V8.3335H30V3.3335H26.6667Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
        </svg>
      </div>
      <div class="logo">
        <svg
          @click="navigateTo('/main')"
          style="cursor: pointer"
          width="60"
          height="25"
          viewBox="0 0 60 25"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M0 11.4349V24.0579C3.77049 24.2218 8.94098 24.1382 12.7869 22.9103C16.8098 21.6251 21.3115 18.9759 23.6066 16.3529V24.0579C27.8689 24.0579 31.3115 24.3857 37.377 22.5824C41.2197 21.4398 44.918 18.812 47.541 16.3529V24.0579H60V0.615234C55.7377 0.779169 55.0639 0.564415 51.1475 1.27097C41.1475 2.74638 40.3459 8.42671 36.3934 9.13982V0.779169C36.3934 0.779169 26.8852 0.287366 21.6393 3.07425C15.0803 6.5595 11.8033 12.5824 0 11.4349Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
          <path
            d="M10.1053 5.05263C6.73684 5.98232 5.98232 6.73684 5.05263 10.1053C4.12295 6.73684 3.36842 5.98232 0 5.05263C3.36842 4.12295 4.12295 3.36842 5.05263 0C5.98232 3.36842 6.73684 4.12295 10.1053 5.05263Z"
            :fill="isDarkMode ? '#75FB9F' : 'black'"
          />
        </svg>
      </div>
    </div>

    <div class="chatbox" :style="{ height: isAnimating ? '100vh' : '365px' }">
      <svg
        :width="svgWidth"
        :height="svgHeight"
        :viewBox="viewBox"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          :d="pathData"
          :fill="isDarkMode ? '#1C1F1C' : 'white'"
          :stroke="isDarkMode ? '#A7A9AC' : '#1463F3'"
          stroke-width="5"
        />
        <foreignObject
          x="0"
          y="0"
          width="100%"
          height="100%"
          style="position: relative"
        >
          <div class="enlarge-btn" @click="startAnimation" tabindex="0">
            <svg
              width="25"
              height="25"
              viewBox="0 0 25 25"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M15.625 3.125H21.875V9.375"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M9.375 21.875H3.125V15.625"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M21.8752 3.125L14.5835 10.4167"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M3.125 21.8747L10.4167 14.583"
                :stroke="isDarkMode ? '#A7A9AC' : 'black'"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
          <div
            class="main"
            :class="isAnimating ? 'enlarge-main' : 'normal-main'"
          >
            <div class="chart-div" v-if="isChartVisible">
              <TheChart
                :company-id="company_id"
                :report-type="report_type"
                :data-field="data_field"
                :chart-data="chartData"
              />
            </div>
            <div xmlns="http://www.w3.org/1999/xhtml" class="text-div">
              <div class="text-block">
                <text
                  class="mark-down-text"
                  :style="{ color: isDarkMode ? '#A7A9AC' : 'black' }"
                  v-html="markdownToHtml"
                ></text>
              </div>
            </div>
          </div>
          <div
            class="chatbox-design"
            :class="isAnimating ? 'enlarge-mode' : 'normal-mode'"
            tabindex="0"
          >
            <svg
              @click="submitRequest"
              style="cursor: pointer"
              width="138"
              height="97"
              viewBox="0 0 138 97"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M30.0119 96.088L16 9.45703L137.967 92.9638L30.0119 96.088Z"
                fill="#A7A9AC"
              />
              <path
                d="M14.0119 90.088L0 3.45703L121.967 86.9638L14.0119 90.088Z"
                fill="#75FB9F"
              />
            </svg>
          </div>
        </foreignObject>
      </svg>
    </div>

    <div class="main-content" v-show="!isAnimating">
      <!-- enterprise  -->

      <div
        class="main-div"
        v-show="!(isEnterprisePressed === false && showMainDiv === false)"
      >
        <!-- original  -->
        <div class="main-div-org" v-if="showMainDiv">
          <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">
            {{ enterpriseText }}
          </p>
          <div class="select-button">
            <svg
              @click="toggleEnterprise"
              style="cursor: pointer"
              width="60"
              height="60"
              viewBox="0 0 60 60"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M30 40L40 30L30 20"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M20 30H40"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
        </div>

        <!-- expand  -->
        <Transition name="slide1">
          <div
            class="enterprise-button-list main-div-expand"
            v-if="isEnterprisePressed"
          >
            <div class="enterprise-scrollable-list">
              <div
                v-for="item in enterpriseItems"
                :key="item.name"
                @click="handleClick(item, 'enterprise')"
                class="enterprise-button list-div"
                tabindex="0"
              >
                {{ item.value }}
              </div>
            </div>
          </div>
        </Transition>
      </div>

      <!-- finacial sheet  -->

      <div
        class="main-div"
        v-show="!(isFinacialPressed === false && showMainDiv === false)"
      >
        <!-- original  -->
        <div class="main-div-org" v-if="showMainDiv">
          <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">
            {{ financialText }}
          </p>
          <div class="select-button">
            <svg
              @click="toggleFinancial"
              style="cursor: pointer"
              width="60"
              height="60"
              viewBox="0 0 60 60"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M30 40L40 30L30 20"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M20 30H40"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
        </div>

        <!-- expand  -->
        <Transition name="slide1">
          <div
            class="financial-button-list financial-main-div-expand"
            v-if="isFinacialPressed"
          >
            <div class="financial-scrollable-list">
              <div
                v-for="item in financialItems"
                :key="item.name"
                @click="handleClick(item, 'financial')"
                class="financial-button list-div"
                tabindex="0"
              >
                {{ item.name }}
              </div>
            </div>
          </div>
        </Transition>
      </div>

      <!-- indicator  -->

      <div
        class="main-div"
        v-show="!(isIndicatorPressed === false && showMainDiv === false)"
      >
        <!-- original  -->
        <div class="main-div-org" v-if="showMainDiv">
          <p :style="{ color: isDarkMode ? '#75FB9F' : 'black' }">
            {{ indicatorText }}
          </p>
          <div class="select-button">
            <svg
              @click="toggleIndicator"
              style="cursor: pointer"
              width="60"
              height="60"
              viewBox="0 0 60 60"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M30 55C43.8071 55 55 43.8071 55 30C55 16.1929 43.8071 5 30 5C16.1929 5 5 16.1929 5 30C5 43.8071 16.1929 55 30 55Z"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M30 40L40 30L30 20"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M20 30H40"
                :stroke="isDarkMode ? '#75FB9F' : 'black'"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
        </div>

        <!-- expand  -->
        <Transition name="slide1">
          <div
            class="indicator-button-list indicator-main-div-expand"
            v-if="isIndicatorPressed"
          >
            <div class="indicator-scrollable-list">
              <div
                v-for="item in selectedIndicators"
                :key="item.name"
                @click="handleClick(item, 'indicators')"
                class="indicator-button list-div"
                tabindex="0"
              >
                {{ item.name }}
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </div>
</template>

<script>
import TheChart from "./TheChart.vue";
import anime from "animejs/lib/anime.es.js";
// import { MarkdownIt } from "vue3-markdown-it";
import { marked } from "marked";

export default {
  data() {
    return {
      isChartVisible: false,
      showMainDiv: true,
      isEnterprisePressed: false,
      isFinacialPressed: false,
      isIndicatorPressed: false,
      isAnimating: false,
      isDarkMode: false,
      svgWidth: 1231,
      svgHeight: 346,
      viewBox: "0 0 1231 346",
      pathData:
        "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z",

      company_id: "",
      report_type: "",
      data_field: "",
      chartData: [],
      summary: "",
      enterpriseText: "ENTERPRISE",
      enterpriseItems: [
        { value: "華南金HNFHC", name: "HNFHC", id: "2880" },
        { value: "富邦金FUBFH", name: "FUBFH", id: "2881" },
        { value: "國泰金CFH", name: "CFH", id: "2882" },
        { value: "開發金KGI", name: "KGI", id: "2883" },
        { value: "玉山金ESFHC", name: "ESFHC", id: "2884" },
        { value: "元大金YFH", name: "YFH", id: "2885" },
        { value: "兆豐金MFG", name: "MFG", id: "2886" },
        { value: "台新金TSFHC", name: "TSFHC", id: "2887" },
        { value: "新光金SKFH", name: "SKFH", id: "2888" },
        { value: "國票金CBFHC", name: "CBFHC", id: "2889" },
        { value: "永豐金SPH", name: "SPH", id: "2890" },
        { value: "中信金CTBC", name: "CTBC", id: "2891" },
        { value: "第一金FFHC", name: "FFHC", id: "2892" },
        { value: "日盛金JSFHC", name: "JSFHC", id: "5820" },
        { value: "合庫金TCFHC", name: "TCFHC", id: "5880" },
      ],
      financialText: "FINANCIAL SHEET",
      financialItems: [
        {
          name: "FINANCIAL INDICATOR",
          id: "financialIndicators",
          value: "indicator",
        },
        {
          name: "INCOME STATEMENT",
          id: "incomeStatement",
          value: "income_statement",
        },
        {
          name: "CASH FLOW STATEMENT",
          id: "cashFlowStatement",
          value: "cash_flow",
        },
        { name: "BALANCE SHEET", id: "balanceSheet", value: "balance_sheet" },
      ],
      indicatorText: "INDICATORS",
      indicatorItems: {
        financialIndicators: [
          // {value:"", name: "#"},
          { value: "ROA(A)稅後息前", name: "ROA(A) After Tax" },
          { value: "ROA－綜合損益", name: "ROA Income" },
          { value: "ROE(A)－稅後", name: "ROE(A) After Tax" },
          { value: "ROE(B)－常續利益", name: "ROE(B) Continuing" },
          { value: "ROE－綜合損益", name: "ROE Income" },
        ],
        incomeStatement: [
          { value: "營業收入淨額", name: "Net Sales" },
          { value: "營業費用", name: "Op. Expenses" },
          { value: "利息收入", name: "Interest Inc." },
          { value: "稅前淨利", name: "Pre-Tax Profit" },
          { value: "所得稅費用", name: "Tax Expense" },
        ],
        cashFlowStatement: [
          { value: "稅前淨利－CFO", name: "Pre-Tax CFO" },
          { value: "折舊－CFO", name: "Depreciation" },
          { value: "攤提－CFO", name: "Amortization" },
          { value: "來自營運之現金流量", name: "Cash Flow Ops" },
          { value: "新增投資－CFI", name: "New Inv. CFI" },
        ],
        balanceSheet: [
          { value: "現金及約當現金", name: "Cash & Equiv." },
          { value: "應收帳款及票據", name: "Accounts Rec." },
          { value: "其他應收款", name: "Other Receiv." },
          { value: "不動產廠房及設備", name: "Prop. & Equip." },
          { value: "商譽及無形資產合計", name: "Goodwill & Int." },
        ],
      },
      selectedIndicators: [], // 儲存選擇的指標
      financialData: {
        data: {
          1409: {
            balance_sheet: [
              [
                {
                  year_month: "20-Mar",
                  現金及約當現金: 11085629.0,
                },
                {
                  year_month: "20-Jun",
                  現金及約當現金: 9919374.0,
                },
                {
                  year_month: "20-Sep",
                  現金及約當現金: 10218352.0,
                },
                {
                  year_month: "20-Dec",
                  現金及約當現金: 11871706.0,
                },
                {
                  year_month: "21-Mar",
                  現金及約當現金: 10171545.0,
                },
                {
                  year_month: "21-Jun",
                  現金及約當現金: 10744259.0,
                },
                {
                  year_month: "21-Sep",
                  現金及約當現金: 9515292.0,
                },
                {
                  year_month: "21-Dec",
                  現金及約當現金: 10284293.0,
                },
              ],
            ],
          },
          1434: {
            balance_sheet: [
              [
                {
                  year_month: "20-Mar",
                  現金及約當現金: 1502777.0,
                },
                {
                  year_month: "20-Jun",
                  現金及約當現金: 2556675.0,
                },
                {
                  year_month: "20-Sep",
                  現金及約當現金: 2919670.0,
                },
                {
                  year_month: "20-Dec",
                  現金及約當現金: 3083322.0,
                },
                {
                  year_month: "21-Mar",
                  現金及約當現金: 2510999.0,
                },
                {
                  year_month: "21-Jun",
                  現金及約當現金: 3056752.0,
                },
                {
                  year_month: "21-Sep",
                  現金及約當現金: 3241609.0,
                },
                {
                  year_month: "21-Dec",
                  現金及約當現金: 3471141.0,
                },
              ],
            ],
          },
        },
      },
    };
  },
  components: {
    TheChart,
  },
  computed: {
    markdownToHtml() {
      return marked(this.summary);
    },
  },
  mounted() {
    const storedDarkMode = sessionStorage.getItem("isDarkMode");
    if (storedDarkMode !== null) {
      this.$isDarkMode = JSON.parse(storedDarkMode);
      this.$nextTick(() => {
        // console.log(this.$isDarkMode);
      });
      // console.log(this.$isDarkMode);
    }
    if (this.$isDarkMode == true) {
      this.isDarkMode = true;
    }
  },
  methods: {
    startAnimation() {
      this.isAnimating = !this.isAnimating;
      if (this.isAnimating) {
        anime({
          targets: this,
          // svgWidth: 1231,
          svgHeight: 727,
          viewBox: [
            { value: "0 0 1231 346" }, // 開始 viewBox
            { value: "0 0 1231 727" }, // 結束 viewBox
          ],
          pathData: [
            {
              value:
                "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z",
            }, // 開始 path
            {
              value:
                "M3 103.92L77.4696 3H1196.01L1227 564.964H1101.05L1156.53 719L1061.57 640.389L35.9865 679.694L3 103.92Z",
            }, // 結束 path
          ],
          easing: "easeInOutQuad",
          duration: 750,
        });
      }
      if (!this.isAnimating) {
        this.pathData =
          "M3 50.5L77.5 3H1196.5L1227.5 267.5H1101.5L1157 340L1062 303L36 321.5L3 50.5Z";
        this.viewBox = "0 0 1231 346";
        this.svgHeight = "346";
      }
    },
    navigateTo(path) {
      // 使用傳遞的路徑導航
      this.$router.push(path);
    },
    toggleEnterprise() {
      this.isEnterprisePressed = !this.isEnterprisePressed;
      this.showMainDiv = false;
    },
    toggleFinancial() {
      this.isFinacialPressed = !this.isFinacialPressed;
      this.showMainDiv = false;
    },
    toggleIndicator() {
      this.isIndicatorPressed = !this.isIndicatorPressed;
      this.showMainDiv = false;
    },
    handleClick(item, type) {
      if (type === "enterprise") {
        this.enterpriseText = item.name;
        this.company_id = item.id;
        this.isEnterprisePressed = !this.isEnterprisePressed;
      } else if (type === "financial") {
        this.financialText = item.name;
        this.report_type = item.value;
        this.selectedIndicators = this.indicatorItems[item.id] || []; // 根據所選的財務表更新指標
        this.isFinacialPressed = !this.isFinacialPressed;
      } else if (type === "indicators") {
        this.indicatorText = item.name;
        this.data_field = item.value;
        this.isIndicatorPressed = !this.isIndicatorPressed;
      }
      this.showMainDiv = true;
    },
    async submitRequest() {
      try {
        const params = {
          company_id: this.company_id,
          report_type: this.report_type,
          data_field: this.data_field,
        };

        console.log("Submitting request with parameters:", params);
        const response = await this.$axios.get(
          "http://127.0.0.1:8000/api/financial_data/",
          { params }
        );
        this.chartData = response.data[this.company_id][this.report_type][0];
        this.isChartVisible = true;
        //
        console.log("Response from server:", response.data);
        // 假設 response.data 的結構如您所示
        const resData = response.data;

        // 構造發送給 financial_indicator_summary 的數據
        const dataToSend = {
          data: {
            [this.company_id]: {
              [this.report_type]: [resData[this.company_id][this.report_type]],
            },
          },
        };

        const analysisResponse = await this.$axios.post(
          "http://127.0.0.1:8000/api/financial_indicator_summary/",
          { data: resData }
        );

        console.log("Analysis result:", analysisResponse.data.analysis);
        this.summary = analysisResponse.data.analysis;
      } catch (error) {
        console.error("Error during request:", error);
      }
    },
  },
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

/* header */
.header {
  position: relative;
  justify-content: center;
  align-items: center;
  height: 6.25vh;
  width: 100%;
  display: flex;
  border: 1px solid black;
}

.back-btn {
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
  cursor: pointer;
}
.logo {
  border-radius: 10px;
  width: 12vw;
  height: 8.15vh;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.chatbox {
  position: relative;
  padding: 1rem 0.5rem 0.5rem 0.5rem;
  justify-content: center;
  align-items: center;
  width: 100%;
  display: flex;
  border: 1px solid black;
  transition: height 0.75s ease;
}

.output-box {
  width: 100%;
  height: auto;
  position: relative;
}

.svg-container {
  transform-origin: top; /* 缩放原点 */
}

.zoom-in {
  transform: scaleY(2); /* 垂直缩放 */
}

.enlarge-btn {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 1rem;
  margin-right: 3rem;
  cursor: pointer;
}
.chart-div {
  height: 60%;
  width: 100%;
  margin-top: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.chatbox-design {
  display: inline-block;
  position: absolute;
  bottom: 0;
  left: 0;

  transition: margin 0.3s ease;
}
.enlarge-mode {
  margin-bottom: 3.5rem;
  margin-left: 2.5rem;
}
.normal-mode {
  margin-bottom: 2.2rem;
  margin-left: 2.2rem;
}
.main {
  width: 100%;
  height: 80%;
  margin-top: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}
.main::-webkit-scrollbar {
  display: none; /* 隱藏滾動條 */
}
.text-div {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 40%;
}

.text-block {
  display: flex;
  width: 550px;
  color: black;
  border-radius: 10px;
  user-select: none;
}

.main-content {
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.main-div {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  border: 1px solid black;
  position: relative;
  align-items: center;
  flex-direction: row;
}

/* .dark-mode .main-div {
  border-color: #75fb9f;
} */

.main-div-org {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.main-div-expand {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  position: relative;
  align-items: flex-start;
  flex-direction: row;
}

.select-button {
  position: absolute;
  right: 80px;
}

/* enterprise-list  */
.enterprise-button-list {
  width: 250px;
  height: 390px;
  overflow-y: auto;
  margin: 15px;
  box-sizing: border-box;
  z-index: 10;
}
.enterprise-button-list::-webkit-scrollbar {
  display: none;
}
.enterprise-scrollable-list {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.enterprise-button {
  cursor: pointer;
}

.enterprise-button:hover {
  /* color: #75fb9f; */
}

/* financial-list  */
.financial-main-div-expand {
  display: flex;
  flex: 1;
  text-align: center;
  justify-content: center;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.financial-button-list {
  width: 250px;
  height: 390px;
  overflow-y: auto;
  margin: 15px;
  box-sizing: border-box;
  z-index: 10;
}
.financial-button-list::-webkit-scrollbar {
  display: none;
}
.financial-scrollable-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.financial-button {
  cursor: pointer;
}
/* indicator */
.indicator-main-div-expand {
  display: flex;
  /* flex: 1; */
  text-align: center;
  justify-content: center;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.indicator-button-list {
  width: 720px;
  height: 390px;
  overflow-y: auto;
  margin: 15px;
  box-sizing: border-box;
  z-index: 10;
}
.indicator-button-list::-webkit-scrollbar {
  display: none;
}
.indicator-scrollable-list {
  display: flex;
  flex-wrap: wrap; /* 允許按鈕換行 */
  max-width: 100%; /* 限制寬度以符合容器 */
}
.indicator-button {
  border-radius: 90px;
  height: 70px; /* 固定高度 */
  width: auto; /* 根據內容長度調整寬度 */
  border: 1px solid #000;
  padding: 5px 10px; /* 增加內邊距以確保內容與邊界有距離 */
  display: inline-block; /* 根據內容大小調整寬度 */
  margin-bottom: 5px; /* 每個按鈕之間的間距 */
  white-space: nowrap; /* 防止文字換行 */
  cursor: pointer;
}

/* Dark-Mode */
.dark-mode {
  background-color: #1b2023;
  transition: ease-out 0.35s;
}
.dark-mode border {
  border: 2px solid #75fb9f;
}

p {
  margin: 0;
  font-family: "Micro5", sans-serif;
  font-style: normal;
  font-weight: 300;
  font-size: 96px;
  user-select: none;
}

.h3,
h3 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-style: bold;
  font-size: 13px !important;
  user-select: none;
}

.list-div {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 200%;
  user-select: none;
  letter-spacing: 0.5em;
  /* color: white; */
}

.dark-mode .list-div {
  color: #75fb9f;
}

@font-face {
  font-family: "Micro5";
  src: url("../assets/fonts/Micro5-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "PressStar2PFont";
  src: url("../assets/fonts/PressStart2P-Regular.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "Inter";
  src: url("../assets/fonts/Inter.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}

/* anime  */
.slide2-enter-active,
.slide2-leave-active {
  transition: all 0.75s ease;
}

.slide2-enter {
  transform: translateY(100%); /* 從下方進入 */
  opacity: 0; /* 透明開始 */
}

.slide2-enter-to {
  transform: translateY(0); /* 最終位置 */
  /* opacity: 1; 最終完全不透明 */
}
.slide2-leave {
  transform: translateY(0); /* 從當前位置開始 */
  /* opacity: 1;  */
}

.slide2-leave-to {
  transform: translateY(100%); /* 向下移動到下方 */
  /* opacity: 0; */
}

.slide1-enter-active {
  transition: all 1s ease;
}
.slide1-leave-active {
}
.slide1-enter {
  transform: translateY(100%);
  opacity: 1;
}
.slide1-leave-to {
  /* transform: translateY(100%); */
}
.slide1-enter-from {
  opacity: 0;
  transform: translateY(100%);
}

.slideMainDiv-enter-active {
  transition: transform 0.75s ease;
}
.slideMainDiv-leave-active {
  transition: transform 0.75s ease;
}
.slideMainDiv-enter {
  transform: translateX(100%);
  opacity: 1;
}
.slideMainDiv-leave-to {
  transform: translateX(100%);
  /* opacity: 0; */
}
.slideMainDiv-enter-from {
  transform: translateX(100%);
  /* opacity: 0; */
}
</style>
<style>
.mark-down-text {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.mark-down-text h3 {
  font-style: bold;
  font-size: 20px !important;
  user-select: none;
}
</style>
