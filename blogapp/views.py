from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q
from django.shortcuts import render


def index(request):

    blogapp = Post.objects.all()
    paginator = Paginator(blogapp, 5)
    page = request.GET.get('page')
    blogapp = paginator.get_page(page)

    return render(request,'index.html', {'blogapp': blogapp})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def search(request):

    query=request.GET.get('q')
    result=Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    return render(request,'index.html',{'blogapp':result})
