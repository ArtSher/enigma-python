from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post



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
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})