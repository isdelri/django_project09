#Register the Post model with the Django admin.

from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)