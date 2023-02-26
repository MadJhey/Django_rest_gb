from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


from .models import Article, Author, Biography, Book, Project, Task, Users
from .serializers import (ArticleModelSerializer, AuthorModelSerializer,
                          BiographyModelSerializer, BookModelSerializer,
                          ProjectModelSerializer, TaskModelSerializer)


class AuthorPogination(LimitOffsetPagination):
    default_limit = 1


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ('id', 'first_name')
    pagination_class = AuthorPogination
    # def get_queryset(self):
    #     # return Author.objects.filter(pk=1)
    #     # return Author.objects.filter(first_name__contains='admin1')
    #     param = self.request.query_params.get('first_name', None)
    #     # http://127.0.0.1:8000/api/authors/?first_name=admin1
    #     if param is not None:
    #         return Author.objects.filter(first_name__contains=param)
    #     else:
    #         # return Author.objects.all()
    #         return super().get_queryset()


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ProjectModelViewSet(ViewSet):

    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def MyProjects(self, request):
        return Response({'data': 'prp'})


class TaskModelViewSet(ViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class MyAPIView(CreateAPIView, ListAPIView):
    # renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
