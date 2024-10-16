from django.db import models

# Create your models here.
class FinancialIndicator(models.Model):
    
    company_id = models.BigIntegerField(db_column='代號')  # 公司代號
    name = models.CharField(max_length=50, db_column='名稱')  # 公司名稱
    year_month = models.CharField(max_length=20, db_column='年－月')  # 年月
    roa_after_tax_before_interest_a = models.DecimalField(max_digits=10, decimal_places=5, db_column='ROA(A)稅後息前%')
    roa_comprehensive = models.DecimalField(max_digits=10, decimal_places=5, db_column='ROA－綜合損益')
    roe_after_tax_a = models.DecimalField(max_digits=10, decimal_places=5, db_column='ROE(A)－稅後')
    roe_continual_profit_b = models.DecimalField(max_digits=10, decimal_places=5, db_column='ROE(B)－常續利益')
    roe_comprehensive = models.DecimalField(max_digits=10, decimal_places=5, db_column='ROE－綜合損益')
    continual_profit_rate_after_tax_a = models.DecimalField(max_digits=10, decimal_places=5, db_column='常續利益率－稅後(A)')
    net_profit_rate_after_tax_a = models.DecimalField(max_digits=10, decimal_places=5, db_column='稅後淨利率(A)')
    continual_eps = models.DecimalField(max_digits=10, decimal_places=5, db_column='常續性每股盈餘')
    revenue_growth_rate_a = models.DecimalField(max_digits=10, decimal_places=5, db_column='營收成長率(A)')
    net_profit_growth_rate = models.DecimalField(max_digits=10, decimal_places=5, db_column='稅後淨利成長率')
    operating_net_profit_growth_rate = models.DecimalField(max_digits=10, decimal_places=5, db_column='經常淨利成長率')
    continual_net_profit_growth_rate = models.DecimalField(max_digits=10, decimal_places=5, db_column='常續淨利成長率')
    total_assets_growth_rate = models.DecimalField(max_digits=10, decimal_places=5, db_column='總資產成長率')
    net_worth_growth_rate = models.DecimalField(max_digits=10, decimal_places=5, db_column='淨值成長率')
    total_liabilities_to_net_worth = models.DecimalField(max_digits=10, decimal_places=5, db_column='總負債/總淨值')
    liabilities_rate = models.DecimalField(max_digits=10, decimal_places=5, db_column='負債比率')
    net_worth_to_assets = models.DecimalField(max_digits=10, decimal_places=5, db_column='淨值/資產')

    class Meta:
        db_table = '金控指標'  # 單一的表格來存放所有公司的指標數據
        managed = True  # Django 自動管理這個表格
        app_label = 'finance_visualizer'

    def __str__(self):
        return f"{self.name} ({self.year_month})"

class IncomeStatement(models.Model):
    company_id = models.BigIntegerField(db_column='代號')  # 公司代號
    name = models.CharField(max_length=50, db_column='名稱')  # 公司名稱
    year_month = models.CharField(max_length=10, db_column='年－月')  # 年月
    net_revenue = models.DecimalField(max_digits=20, decimal_places=5, db_column='營業收入淨額')  # 營業收入淨額
    operating_expense = models.DecimalField(max_digits=20, decimal_places=5, db_column='營業費用')  # 營業費用
    interest_income = models.DecimalField(max_digits=20, decimal_places=5, db_column='利息收入')  # 利息收入
    pre_tax_profit = models.DecimalField(max_digits=20, decimal_places=5, db_column='稅前淨利')  # 稅前淨利
    income_tax_expense = models.DecimalField(max_digits=20, decimal_places=5, db_column='所得稅費用')  # 所得稅費用
    consolidated_total_profit_loss = models.DecimalField(max_digits=20, decimal_places=5, db_column='合併總損益')  # 合併總損益
    other_comprehensive_income_oci = models.DecimalField(max_digits=20, decimal_places=5, db_column='其他綜合損益－OCI')  # 其他綜合損益 - OCI
    total_comprehensive_income = models.DecimalField(max_digits=20, decimal_places=5, db_column='本期綜合損益總額')  # 本期綜合損益總額
    earnings_per_share = models.DecimalField(max_digits=10, decimal_places=5, db_column='每股盈餘')  # 每股盈餘
    weighted_average_shares = models.BigIntegerField(db_column='加權平均股數')  # 加權平均股數
    special_stock_dividend = models.DecimalField(max_digits=10, decimal_places=5, db_column='發放特別股股息')  # 發放特別股股息
    continuous_net_profit_after_tax = models.DecimalField(max_digits=20, decimal_places=5, db_column='常續性稅後淨利')  # 常續性稅後淨利

    class Meta:
        db_table = '金控損益表'
        managed = True  # 如果你想手動管理資料庫表結構，設為 False；如果想由 Django 自動管理，設為 True
        app_label = 'finance_visualizer'

class CashFlowStatement(models.Model):
    code = models.CharField(max_length=10, verbose_name="代號")  # 例如 '2880', '2881' 等金融機構代號
    name = models.CharField(max_length=50, verbose_name="名稱")  # 公司名稱
    year_month = models.CharField(max_length=10, verbose_name="年－月")  # 期間，格式如 '23-Dec'
    profit_before_tax_cfo = models.BigIntegerField(verbose_name="稅前淨利－CFO")  # 稅前淨利
    depreciation_cfo = models.BigIntegerField(verbose_name="折舊－CFO")  # 折舊
    amortization_cfo = models.BigIntegerField(verbose_name="攤提－CFO")  # 攤提
    cash_flow_from_operations = models.BigIntegerField(verbose_name="來自營運之現金流量")  # 營運現金流
    new_investment_cfi = models.BigIntegerField(verbose_name="新增投資－CFI", null=True, blank=True)  # 新增投資
    investment_sale_cfi = models.BigIntegerField(verbose_name="出售投資－CFI", null=True, blank=True)  # 出售投資
    purchase_property_cfi = models.BigIntegerField(verbose_name="購置不動產廠房設備－CFI", null=True, blank=True)  # 購置不動產
    property_disposal_cfi = models.BigIntegerField(verbose_name="處分不動產廠房設備－CFI", null=True, blank=True)  # 處分不動產
    cash_flow_from_investments = models.BigIntegerField(verbose_name="投資活動之現金流量")  # 投資現金流
    capital_increase_cff = models.BigIntegerField(verbose_name="現金增（減）資－CFF")  # 現金增資
    cash_dividends_cff = models.BigIntegerField(verbose_name="支付現金股利－CFF")  # 支付現金股利
    cash_flow_from_financing = models.BigIntegerField(verbose_name="籌資活動之現金流量")  # 籌資現金流
    foreign_exchange_effect = models.BigIntegerField(verbose_name="匯率影響數")  # 匯率影響
    net_cash_flow = models.BigIntegerField(verbose_name="本期產生現金流量")  # 本期現金流
    cash_beginning = models.BigIntegerField(verbose_name="期初現金及約當現金")  # 期初現金
    cash_ending = models.BigIntegerField(verbose_name="期末現金及約當現金")  # 期末現金

    class Meta:
        db_table = '金控現金流量表'
        managed = True
        app_label = 'finance_visualizer'

    def __str__(self):
        return f"{self.name} ({self.year_month})"

class BalanceSheet(models.Model):
    code = models.CharField(max_length=10, verbose_name="代號")
    name = models.CharField(max_length=50, verbose_name="名稱")
    year_month = models.CharField(max_length=10, verbose_name="年－月")
    cash_and_cash_equivalents = models.BigIntegerField(verbose_name="現金及約當現金")
    accounts_receivable = models.BigIntegerField(verbose_name="應收帳款及票據")
    other_receivables = models.BigIntegerField(verbose_name="其他應收款")
    property_plant_and_equipment = models.BigIntegerField(verbose_name="不動產廠房及設備")
    goodwill_and_intangibles = models.BigIntegerField(verbose_name="商譽及無形資產合計")
    right_of_use_assets = models.BigIntegerField(verbose_name="使用權資產")
    investment_property_net = models.BigIntegerField(verbose_name="投資性不動產淨額")
    other_non_current_assets = models.BigIntegerField(verbose_name="其他非流動資產")
    total_assets = models.BigIntegerField(verbose_name="資產總額")
    accounts_payable = models.BigIntegerField(verbose_name="應付帳款及票據")
    other_payables = models.BigIntegerField(verbose_name="其他應付款")
    special_stock_liabilities_non_current = models.BigIntegerField(verbose_name="特別股負債－非流動", null=True, blank=True)
    non_current_liabilities_bonds = models.BigIntegerField(verbose_name="應付公司債－非流動", null=True, blank=True)
    non_current_borrowings = models.BigIntegerField(verbose_name="其他長期借款－非流動")
    non_current_lease_liabilities = models.BigIntegerField(verbose_name="租賃負債－非流動")
    provisions_non_current = models.BigIntegerField(verbose_name="負債準備－非流動")
    total_liabilities = models.BigIntegerField(verbose_name="負債總額")
    common_stock = models.BigIntegerField(verbose_name="普通股股本")
    special_stock = models.BigIntegerField(verbose_name="特別股股本", null=True, blank=True)
    received_in_advance_for_stock = models.BigIntegerField(verbose_name="預收股款", null=True, blank=True)
    dividends_distributable = models.BigIntegerField(verbose_name="待分配股票股利", null=True, blank=True)
    capital_surplus = models.BigIntegerField(verbose_name="資本公積合計")
    retained_earnings = models.BigIntegerField(verbose_name="保留盈餘")
    other_equity = models.BigIntegerField(verbose_name="其他權益")
    treasury_stock = models.BigIntegerField(verbose_name="庫藏股票帳面值", null=True, blank=True)
    total_equity = models.BigIntegerField(verbose_name="股東權益總額")
    total_liabilities_and_equity = models.BigIntegerField(verbose_name="負債及股東權益總額")

    class Meta:
        db_table = '金控資產負債表'
        managed = True
        app_label = 'finance_visualizer'

    def __str__(self):
        return f"{self.name} ({self.year_month})"