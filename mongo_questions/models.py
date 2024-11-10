from django.db import models

class NewsQuestion(models.Model):
    """
    用於新聞題型的模型
    """
    summary = models.TextField()
    question = models.TextField()
    options = models.JSONField()  # 選項作為 JSON 格式存儲
    difficulty = models.CharField(max_length=1)  # 難度：1, 2, 3
    source = models.TextField()
    url = models.URLField()

    class Meta:
        db_table = "news_questions"
        app_label = 'mongo_questions'

class BasicsQuestion(models.Model):
    """
    用於基礎題型的模型
    """
    question = models.TextField()
    options = models.JSONField()  # 選項作為 JSON 格式存儲
    difficulty = models.CharField(max_length=1)  # 難度：1, 2, 3
    type = models.CharField(max_length=100)

    class Meta:
        db_table = "basics_questions"
        app_label = 'mongo_questions'