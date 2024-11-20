from django.contrib import admin
from .models import Post, Category


class CategoryInline(admin.TabularInline):  
    model = Category.posts.through 
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    list_display = ('name', 'description')
    search_fields = ('name',)