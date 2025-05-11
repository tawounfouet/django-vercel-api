# content/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UserProfileViewSet, CategoryViewSet, TagViewSet,
    PostViewSet, PodcastViewSet, VideoViewSet, CommentViewSet,
    # api_root
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # path('', api_root, name='api-root'),
    path('', include(router.urls)),
]