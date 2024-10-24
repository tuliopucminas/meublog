from django.contrib import admin

from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title','id']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post']
    search_fields = ['author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
