from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Tag
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_search(request):
    query = request.GET.get('q')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

def posts_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.all()
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})
