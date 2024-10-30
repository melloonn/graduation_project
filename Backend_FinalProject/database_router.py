class FinancialDataRouter:
    """
    財報數據的數據庫路由器：
    
    - db_for_read: 指定讀取數據的資料庫。
    - db_for_write: 指定寫入數據的資料庫。
    - allow_relation: 允許哪些模型之間的關聯。
    - allow_migrate: 決定哪些模型可以被遷移到哪個資料庫。
    """

    def db_for_read(self, model, **hints):
        """
        指定讀取數據的資料庫，若模型屬於 'finance_visualizer' 應用，則使用 'financial_data' 資料庫。
        """
        if model._meta.app_label == 'finance_visualizer':
            return 'financial_data'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        指定寫入數據的資料庫。
        若模型屬於 'finance_visualizer' 應用，則使用 'financial_data' 資料庫。
        """
        if model._meta.app_label == 'finance_visualizer':
            return 'financial_data'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        允許 'finance_visualizer' 應用的模型與其他模型之間的關聯。
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
        return db == 'default'