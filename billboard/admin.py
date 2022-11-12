from django.contrib import admin

from .forms import PostCreateForm
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostCreateForm


admin.site.register(Category)
admin.site.register(Comment)
