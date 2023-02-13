from .models import Users
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Biography, Book, Article, Project, Task


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ['id']


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'fist_name', 'last_name', 'email')


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TaskModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
