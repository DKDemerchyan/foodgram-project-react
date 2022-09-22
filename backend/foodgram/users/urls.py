from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet


router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]