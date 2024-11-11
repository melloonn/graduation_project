from pymongo import MongoClient
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 初始化 MongoDB 連線
client = MongoClient(
    host=settings.MONGO_DB_SETTINGS['HOST'],
    username=settings.MONGO_DB_SETTINGS['USERNAME'],
    password=settings.MONGO_DB_SETTINGS['PASSWORD']
)
mongo_db = client[settings.MONGO_DB_SETTINGS['DB_NAME']]

class NewsQuestionsAPIView(APIView):
    """
    根據難度返回新聞題型
    """
    def get(self, request):
        difficulty = request.query_params.get('difficulty')
        if not difficulty:
            return Response({"error": "Difficulty is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 查詢 MongoDB 的 news_questions 集合
        news_questions_collection = mongo_db['news_questions']
        questions = list(news_questions_collection.find({"difficulty": difficulty}))

        # 格式化回傳數據
        data = [
            {
                "summary": q.get("summary", ""),
                "question": q.get("question", ""),
                "options": q.get("options", []),
                "difficulty": q.get("difficulty", ""),
                "source": q.get("source", ""),
                "url": q.get("url", "")
            } for q in questions
        ]
        return Response(data, status=status.HTTP_200_OK)

class BasicsQuestionsAPIView(APIView):
    """
    根據難度返回基礎題型
    """
    def get(self, request):
        difficulty = request.query_params.get('difficulty')
        if not difficulty:
            return Response({"error": "Difficulty is required"}, status=status.HTTP_400_BAD_REQUEST)

        # 查詢 MongoDB 的 basics_questions 集合
        basics_questions_collection = mongo_db['basics_questions']
        questions = list(basics_questions_collection.find({"difficulty": difficulty}))

        # 格式化回傳數據
        data = [
            {
                "question": q.get("question", ""),
                "options": q.get("options", []),
                "difficulty": q.get("difficulty", ""),
                "type": q.get("type", "")
            } for q in questions
        ]
        return Response(data, status=status.HTTP_200_OK)