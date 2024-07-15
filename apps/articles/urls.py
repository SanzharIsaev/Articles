from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleCreateAPIView ,PublicArticleListAPIView, PublicArticleRetrieveUpdateDestroyAPIView, PrivateArticleListAPIView, PrivateArticleRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register(r'articles', ArticleCreateAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('public_articles/', PublicArticleListAPIView.as_view()),
    path('public_articles/<int:pk>/', PublicArticleRetrieveUpdateDestroyAPIView.as_view()),
    path('private_articles/', PrivateArticleListAPIView.as_view()),
    path('private_articles/<int:pk>/', PrivateArticleRetrieveUpdateDestroyAPIView.as_view()),
]