def get_python_field_name(self, model_class, db_column_name):
        for field in model_class._meta.fields:
            if field.db_column == db_column_name:
                return field.name
        print(f"Could not find matching field for db_column_name '{db_column_name}'")
        return None