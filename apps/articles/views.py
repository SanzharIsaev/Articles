from rest_framework import permissions, generics, viewsets

from .models import Article
from .serializers import ArticleSerializer
from config.permissions import IsOwnerOrReadOnly, IsAuthor


class ArticleCreateAPIView(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthor, permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class PublicArticleListAPIView(generics.ListAPIView):
    
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PublicArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthor, IsOwnerOrReadOnly,)
    

class PrivateArticleListAPIView(generics.ListAPIView):
    
    queryset = Article.objects.filter(is_public=False)
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    
    
class PrivateArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Article.objects.filter(is_public=False)
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, IsAuthor,)