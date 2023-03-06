
from django.contrib import admin
from django.urls import path, include
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet, ProjectModelViewSet, TaskModelViewSet, MyAPIView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'authors', AuthorModelViewSet)
router.register(r'books', BookModelViewSet)
router.register(r'biography', BiographyModelViewSet)
router.register(r'article', ArticleModelViewSet)

myrouter = DefaultRouter()
myrouter.register(r'project', ProjectModelViewSet)
myrouter.register(r'task', TaskModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/', include(router.urls)),
    # path('myapi/', MyAPIView.as_view()),
    path('myapi/', include(myrouter.urls)),
    path('myproject/', ProjectModelViewSet.as_view({'get': 'list'})),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
