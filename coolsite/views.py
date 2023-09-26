from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
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
