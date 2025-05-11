# content/views.py
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Tag, UserProfile, Post, Comment, Podcast, Video
from .serializers import (
    UserSerializer, UserProfileSerializer, CategorySerializer, TagSerializer,
    PostListSerializer, PostDetailSerializer, CommentSerializer,
    PodcastListSerializer, PodcastDetailSerializer, 
    VideoListSerializer, VideoDetailSerializer
)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'user__email', 'role']

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True).order_by('-published_at')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categories__slug', 'tags__slug', 'author__username', 'is_featured']
    search_fields = ['title', 'content', 'excerpt']
    lookup_field = 'slug'
    
    # Ajouter cette propriété pour désactiver le formulaire de filtrage
    #filter_form_template = None
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostListSerializer

class PodcastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Podcast.objects.filter(is_published=True).order_by('-published_at')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categories__slug', 'host__username', 'is_featured', 'season', 'episode']
    search_fields = ['title', 'description']
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PodcastDetailSerializer
        return PodcastListSerializer

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.filter(is_published=True).order_by('-published_at')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categories__slug', 'presenter__username', 'is_featured']
    search_fields = ['title', 'description']
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VideoDetailSerializer
        return VideoListSerializer

class CommentViewSet(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)