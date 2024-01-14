from django.shortcuts import render

# Create your views here.
from .models import Post


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    context = {"post": post}
    return render(request, 'blog/post.html', context)
