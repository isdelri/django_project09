# blogging/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """View to list all blog posts."""
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'blogging/list.html', {'posts': posts})

def post_detail(request, post_id):
    """View to display details of a single blog post."""
    post = get_object_or_404(Post, pk=post_id)  # Get the specific post by ID or return 404
    return render(request, 'blogging/detail.html', {'post': post})
