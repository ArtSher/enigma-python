from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm, CommentForm
from .models import Post, Comment



menu = [
    {'url_name': 'syntax', 'title': 'Синтаксис'},
    {'url_name': 'web', 'title': 'Web'},
    {'url_name': 'ml', 'title': 'ML'},
    {'url_name': 'book', 'title': 'Книги'},
    {'url_name': 'forum', 'title': 'Форум'}
]


def index(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'post': post, 'menu': menu})


def syntax(request):
    pass


def web(request):
    pass


def ml(request):
    pass


def book(request):
    pass


def forum(request):
    pass


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})