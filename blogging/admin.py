#Register the Post model with the Django admin.

from django.contrib import admin
from .models import Post

admin.site.register(Post)

