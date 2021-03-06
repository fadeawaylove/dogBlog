from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "url", "post", "create_time"]
    fields = ['name', 'email', 'url', 'text', 'post']

admin.site.register(Comment, CommentAdmin)
