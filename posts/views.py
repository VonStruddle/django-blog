from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/home.html', {'posts': posts})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'posts/post_detail.html', {'post': post})
