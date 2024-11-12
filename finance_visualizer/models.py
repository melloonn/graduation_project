from django.db import models

class FinancialIndicator(models.Model):
    company_id = models.BigIntegerField(primary_key=True, db_column='代號')
    name = models.CharField(max_length=50, db_column='名稱', default='')
    year_month = models.CharField(max_length=20, db_column='年－月', default='')
    roa_after_tax = models.DecimalField(max_digits=15, decimal_places=2, db_column='ROA(A)稅後息前%', default=0)
    roa_comprehensive = models.DecimalField(max_digits=15, decimal_places=2, db_column='ROA－綜合損益', default=0)
    roe_after_tax = models.DecimalField(max_digits=15, decimal_places=2, db_column='ROE(A)－稅後', default=0)
    roe_continued = models.DecimalField(max_digits=15, decimal_places=2, db_column='ROE(B)－常續利益', default=0)
    roe_comprehensive = models.DecimalField(max_digits=15, decimal_places=2, db_column='ROE－綜合損益', default=0)
    continued_profit_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='常續利益率－稅後(A)', default=0)
    net_profit_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='稅後淨利率(A)', default=0)
    continued_eps = models.DecimalField(max_digits=15, decimal_places=2, db_column='常續性每股盈餘', default=0)
    revenue_growth_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='營收成長率(A)', default=0)
    net_profit_growth_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='稅後淨利成長率', default=0)
    operating_profit_growth_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='經常淨利成長率', default=0)
    continued_net_profit_growth_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='常續淨利成長率', default=0)
    total_assets_growth_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='總資產成長率', default=0)
    net_worth_growth_rate = models.DecimalField(max_digits=15, decimal_places=2, db_column='淨值成長率', default=0)
    total_liabilities_to_net_worth = models.DecimalField(max_digits=15, decimal_places=2, db_column='總負債/總淨值', default=0)
    debt_ratio = models.DecimalField(max_digits=15, decimal_places=2, db_column='負債比率', default=0)
    net_worth_to_assets = models.DecimalField(max_digits=15, decimal_places=2, db_column='淨值/資產', default=0)

    class Meta:
        db_table = '指標'
        managed = True
        app_label = 'finance_visualizer'
        unique_together = (('company_id', 'year_month'),)  # 設置唯一組合

    def __str__(self):
        return f"{self.name} ({self.year_month})"

class IncomeStatement(models.Model):
    company_id = models.BigIntegerField(db_column='代號', primary_key=True) 
    name = models.CharField(max_length=50, db_column='名稱', default='')
    year_month = models.CharField(max_length=20, db_column='年－月', default='')
    net_operating_income = models.DecimalField(max_digits=15, decimal_places=2, db_column='營業收入淨額', default=0)
    operating_expenses = models.DecimalField(max_digits=15, decimal_places=2, db_column='營業費用', default=0)
    interest_income = models.DecimalField(max_digits=15, decimal_places=2, db_column='利息收入', default=0)
    pre_tax_profit = models.DecimalField(max_digits=15, decimal_places=2, db_column='稅前淨利', default=0)
    income_tax_expense = models.DecimalField(max_digits=15, decimal_places=2, db_column='所得稅費用', default=0)
    consolidated_total_income = models.DecimalField(max_digits=15, decimal_places=2, db_column='合併總損益', default=0)
    other_comprehensive_income = models.DecimalField(max_digits=15, decimal_places=2, db_column='其他綜合損益－OCI', default=0)
    total_comprehensive_income = models.DecimalField(max_digits=15, decimal_places=2, db_column='本期綜合損益總額', default=0)
    earnings_per_share = models.DecimalField(max_digits=10, decimal_places=5, db_column='每股盈餘', default=0)
    weighted_average_shares = models.DecimalField(max_digits=15, decimal_places=2, db_column='加權平均股數', default=0)
    special_dividends = models.DecimalField(max_digits=15, decimal_places=2, db_column='發放特別股股息', default=0)
    continual_net_income_after_tax = models.DecimalField(max_digits=15, decimal_places=2, db_column='常續性稅後淨利', default=0)

    class Meta:
        db_table = '損益表'
        managed = True
        app_label = 'finance_visualizer'
        unique_together = ('company_id', 'year_month')


class CashFlowStatement(models.Model):
    company_id = models.BigIntegerField(db_column='代號', primary_key=True)  # 設定 company_id 為主鍵
    name = models.CharField(max_length=50, db_column='名稱', default='')
    year_month = models.CharField(max_length=20, db_column='年－月', default='')
    pre_tax_net_profit_cfo = models.DecimalField(max_digits=15, decimal_places=2, db_column='稅前淨利－CFO', default=0)
    depreciation_cfo = models.DecimalField(max_digits=15, decimal_places=2, db_column='折舊－CFO', default=0)
    amortization_cfo = models.DecimalField(max_digits=15, decimal_places=2, db_column='攤提－CFO', default=0)
    cash_flows_from_operations = models.DecimalField(max_digits=15, decimal_places=2, db_column='來自營運之現金流量', default=0)
    new_investment_cfi = models.DecimalField(max_digits=15, decimal_places=2, db_column='新增投資－CFI', default=0)
    investment_sale_cfi = models.DecimalField(max_digits=15, decimal_places=2, db_column='出售投資－CFI', default=0)
    purchase_property_plant_equipment_cfi = models.DecimalField(max_digits=15, decimal_places=2, db_column='購置不動產廠房設備－CFI', default=0)
    sale_property_plant_equipment_cfi = models.DecimalField(max_digits=15, decimal_places=2, db_column='處分不動產廠房設備－CFI', default=0)
    cash_flows_from_investment = models.DecimalField(max_digits=15, decimal_places=2, db_column='投資活動之現金流量', default=0)
    cash_increase_financing_cff = models.DecimalField(max_digits=15, decimal_places=2, db_column='現金增（減）資－CFF', default=0)
    cash_dividends_cff = models.DecimalField(max_digits=15, decimal_places=2, db_column='支付現金股利－CFF', default=0)
    cash_flows_from_financing = models.DecimalField(max_digits=15, decimal_places=2, db_column='籌資活動之現金流量', default=0)
    foreign_exchange_effect = models.DecimalField(max_digits=15, decimal_places=2, db_column='匯率影響數', default=0)
    cash_flows_for_period = models.DecimalField(max_digits=15, decimal_places=2, db_column='本期產生現金流量', default=0)
    beginning_cash = models.DecimalField(max_digits=15, decimal_places=2, db_column='期初現金及約當現金', default=0)
    ending_cash = models.DecimalField(max_digits=15, decimal_places=2, db_column='期末現金及約當現金', default=0)

    class Meta:
        db_table = '現金流量表'
        managed = True
        app_label = 'finance_visualizer'
        unique_together = ('company_id', 'year_month')


class BalanceSheet(models.Model):
    company_id = models.BigIntegerField(db_column='代號', primary_key=True)  # 設定 company_id 為主鍵
    name = models.CharField(max_length=50, db_column='名稱', default='')
    year_month = models.CharField(max_length=20, db_column='年－月', default='')
    cash_and_equivalents = models.DecimalField(max_digits=15, decimal_places=2, db_column='現金及約當現金', default=0)
    accounts_receivable = models.DecimalField(max_digits=15, decimal_places=2, db_column='應收帳款及票據', default=0)
    other_receivables = models.DecimalField(max_digits=15, decimal_places=2, db_column='其他應收款', default=0)
    property_plant_equipment = models.DecimalField(max_digits=15, decimal_places=2, db_column='不動產廠房及設備', default=0)
    goodwill_and_intangibles = models.DecimalField(max_digits=15, decimal_places=2, db_column='商譽及無形資產合計', default=0)
    right_of_use_assets = models.DecimalField(max_digits=15, decimal_places=2, db_column='使用權資產', default=0)
    investment_property = models.DecimalField(max_digits=15, decimal_places=2, db_column='投資性不動產淨額', default=0)
    other_non_current_assets = models.DecimalField(max_digits=15, decimal_places=2, db_column='其他非流動資產', default=0)
    total_assets = models.DecimalField(max_digits=15, decimal_places=2, db_column='資產總額', default=0)
    accounts_payable = models.DecimalField(max_digits=15, decimal_places=2, db_column='應付帳款及票據', default=0)
    other_payables = models.DecimalField(max_digits=15, decimal_places=2, db_column='其他應付款', default=0)
    preferred_stock_liabilities = models.DecimalField(max_digits=15, decimal_places=2, db_column='特別股負債－非流動', default=0)
    bonds_payable = models.DecimalField(max_digits=15, decimal_places=2, db_column='應付公司債－非流動', default=0)
    other_long_term_loans = models.DecimalField(max_digits=15, decimal_places=2, db_column='其他長期借款－非流動', default=0)
    lease_liabilities = models.DecimalField(max_digits=15, decimal_places=2, db_column='租賃負債－非流動', default=0)
    provisions = models.DecimalField(max_digits=15, decimal_places=2, db_column='負債準備－非流動', default=0)
    total_liabilities = models.DecimalField(max_digits=15, decimal_places=2, db_column='負債總額', default=0)
    common_stock = models.DecimalField(max_digits=15, decimal_places=2, db_column='普通股股本', default=0)
    preferred_stock = models.DecimalField(max_digits=15, decimal_places=2, db_column='特別股股本', default=0)
    pre_received_stock_payments = models.DecimalField(max_digits=15, decimal_places=2, db_column='預收股款', default=0)
    stock_dividends_payable = models.DecimalField(max_digits=15, decimal_places=2, db_column='待分配股票股利', default=0)
    total_stock = models.DecimalField(max_digits=15, decimal_places=2, db_column='股本', default=0)
    additional_paid_in_capital = models.DecimalField(max_digits=15, decimal_places=2, db_column='資本公積合計', default=0)
    retained_earnings = models.DecimalField(max_digits=15, decimal_places=2, db_column='保留盈餘', default=0)
    other_equity = models.DecimalField(max_digits=15, decimal_places=2, db_column='其他權益', default=0)
    treasury_stock = models.DecimalField(max_digits=15, decimal_places=2, db_column='庫藏股票帳面值', default=0)
    total_equity = models.DecimalField(max_digits=15, decimal_places=2, db_column='股東權益總額', default=0)
    total_liabilities_and_equity = models.DecimalField(max_digits=15, decimal_places=2, db_column='負債及股東權益總額', default=0)

    class Meta:
        db_table = '資產負債表'
        managed = True
        app_label = 'finance_visualizer'
        unique_together = ('company_id', 'year_month')

class FinancialReportSummary(models.Model):
    name = models.CharField(max_length=255, primary_key=True)  # 設置 name 為主鍵
    content = models.TextField()

    class Meta:
        db_table = '財報摘要總結'
        managed = True
        app_label = 'finance_visualizer'

    def __str__(self):
        return self.name