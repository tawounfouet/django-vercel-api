# content/admin.py
from django.contrib import admin
from .models import Category, Tag, UserProfile, Post, Comment, Podcast, Video

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'website')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'bio')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured', 'categories')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    filter_horizontal = ('categories', 'tags')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'content')
    date_hierarchy = 'created_at'

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'season', 'episode', 'published_at', 'is_published')
    list_filter = ('is_published', 'is_featured', 'season', 'categories')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    filter_horizontal = ('guests', 'categories')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'presenter', 'published_at', 'is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured', 'categories')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    filter_horizontal = ('categories',)