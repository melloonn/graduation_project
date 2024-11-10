from django.urls import path
from .views import NewsQuestionsAPIView, BasicsQuestionsAPIView

urlpatterns = [
    path('news_questions/', NewsQuestionsAPIView.as_view(), name='news_questions'),
    path('basics_questions/', BasicsQuestionsAPIView.as_view(), name='basics_questions'),
]