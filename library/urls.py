
from django.contrib import admin
from django.urls import path, include
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet, ProjectModelViewSet, TaskModelViewSet, MyAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorModelViewSet)
router.register(r'book', BookModelViewSet)
router.register(r'biography', BiographyModelViewSet)
router.register(r'article', ArticleModelViewSet)
router.register(r'project', ProjectModelViewSet)
router.register(r'task', TaskModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('myapi/', MyAPIView.as_view()),

]
