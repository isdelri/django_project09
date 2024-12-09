from django.urls import path
from blogging.views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),  # Home page
    path('posts/', BlogListView.as_view(), name="blog_list"),  # List all posts
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),  # Blog post detail
]