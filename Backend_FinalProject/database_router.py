class FinancialDataRouter:
    """
    一個負責財報數據的數據庫路由器。

    - db_for_read: 決定從哪個數據庫讀取數據。
    - db_for_write: 決定數據寫入哪個數據庫（雖然此專案不會寫入）。
    - allow_relation: 決定哪些模型之間允許關聯。
    - allow_migrate: 決定哪些模型應該被遷移到哪個數據庫。
    """

    def db_for_read(self, model, **hints):
        """
        如果模型屬於 'finance_visualizer' 應用，從 'financial_data' 資料庫讀取數據。
        """
        if model._meta.app_label == 'finance_visualizer':
            return 'financial_data'
        return None

    def db_for_write(self, model, **hints):
        """
        如果模型屬於 'finance_visualizer' 應用，則不允許寫入。
        （因為本專案不涉及寫入操作）
        """
        if model._meta.app_label == 'finance_visualizer':
            # return None
            return 'financial_data'
        return None 

    def allow_relation(self, obj1, obj2, **hints):
        """
        允許與 'finance_visualizer' 應用相關的模型之間的關聯。
        """
        if (
            obj1._meta.app_label == 'finance_visualizer' or
            obj2._meta.app_label == 'finance_visualizer'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        確保 'finance_visualizer' 應用的模型只遷移到 'financial_data' 資料庫。
        """
        if app_label == 'finance_visualizer':
            return db == 'financial_data'
        return None