# content/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Tag, UserProfile, Post, Comment, Podcast, Video

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'avatar', 'bio', 'website', 'twitter', 'github', 'linkedin', 'role'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']

class PostListSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(source='author.profile', read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'featured_image',
            'published_at', 'author', 'categories', 
            'likes_count', 'reading_time', 'is_featured'
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(source='author.profile', read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'featured_image',
            'published_at', 'updated_at', 'author', 'categories', 'tags',
            'comments', 'likes_count', 'reading_time', 'is_featured', 'is_published'
        ]

class PodcastListSerializer(serializers.ModelSerializer):
    host = UserProfileSerializer(source='host.profile', read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Podcast
        fields = [
            'id', 'title', 'slug', 'description', 'cover_image',
            'duration', 'published_at', 'host', 'categories',
            'plays_count', 'is_featured', 'season', 'episode'
        ]

class PodcastDetailSerializer(serializers.ModelSerializer):
    host = UserProfileSerializer(source='host.profile', read_only=True)
    guests = UserProfileSerializer(source='guests.profile', many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Podcast
        fields = [
            'id', 'title', 'slug', 'description', 'audio_file',
            'duration', 'cover_image', 'published_at', 'updated_at',
            'host', 'guests', 'categories', 'plays_count',
            'is_featured', 'is_published', 'transcript', 'season', 'episode'
        ]

class VideoListSerializer(serializers.ModelSerializer):
    presenter = UserProfileSerializer(source='presenter.profile', read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'slug', 'description', 'thumbnail',
            'duration', 'published_at', 'presenter', 'categories',
            'views_count', 'likes_count', 'is_featured'
        ]

class VideoDetailSerializer(serializers.ModelSerializer):
    presenter = UserProfileSerializer(source='presenter.profile', read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'slug', 'description', 'video_url',
            'thumbnail', 'duration', 'published_at', 'updated_at',
            'presenter', 'categories', 'views_count', 'likes_count',
            'is_featured', 'is_published', 'transcript'
        ]