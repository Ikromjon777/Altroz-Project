from django.contrib import admin
from .models import Category, News, Comment
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category' ,'slug', 'publish_time', 'status']
    list_filter = ['status', 'create_time', 'publish_time']
    prepopulated_fields = {"slug":('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news','name', 'email', 'created_time', 'activate']
    list_filter = ['created_time', 'activate']
    search_fields = ['name','text']
    actions = ['disable_comments', 'activate_comments']
    def disable_comments(self, request, queryset):
        queryset.update(activate=False)
    def activate_comments(self, request, queryset):
        queryset.update(activate=True)