from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Article, Author, Biography, Book, Project, Task, Users
from .serializers import (ArticleModelSerializer, AuthorModelSerializer,
                          BiographyModelSerializer, BookModelSerializer,
                          ProjectModelSerializer, TaskModelSerializer)


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class MyAPIView(APIView):

    def get(self, request, format=None):
        return Response({'message': 'Hello, get!'})

    def post(self, request, format=None):
        return Response({'message': 'Hello, post!'})
