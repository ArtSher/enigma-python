from django.contrib import admin
from .models import Post, Comment, TagPost


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine, ]
    list_display = ('title', 'choice', 'created_date', )
    list_display_links = ('title', 'choice')
    search_fields = ['title']
    filter_vertical = ['tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_date', )
    list_display_links = ('text', )


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('tag', 'slug')
    list_display_links = ('tag', 'slug')