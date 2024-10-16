from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # 如果需要這些字段，請取消註釋
    

    def __str__(self):
        return self.username

