from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import slugify

from .forms import PostForm, CommentForm, TagForm
from .models import Post, Comment, TagPost



menu = [
    {'url_name': 'syntax', 'title': 'Синтаксис'},
    {'url_name': 'web', 'title': 'Web'},
    {'url_name': 'ml', 'title': 'ML'},
    {'url_name': 'book', 'title': 'Книги'},
    {'url_name': 'forum', 'title': 'Форум'}
]


def index(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    tags = TagPost.objects.all()
    context = {
        'post': post,
        'tags': tags,
        'menu': menu
    }
    return render(request, 'blog/index.html', context=context)


def syntax(request):
    post = Post.objects.filter(choice='Syntax').order_by('-published_date')
    tags = TagPost.objects.all()
    context = {
        'post': post,
        'tags': tags,
        'menu': menu
    }
    return render(request, 'blog/index.html', context=context)


def web(request):
    post = Post.objects.filter(choice='Web').order_by('-published_date')
    return render(request, 'blog/index.html', {'post': post, 'menu': menu})


def ml(request):
    post = Post.objects.filter(choice='ML').order_by('-published_date')
    return render(request, 'blog/index.html', {'post': post, 'menu': menu})


def book(request):
    post = Post.objects.filter(choice='Book').order_by('-published_date')
    return render(request, 'blog/index.html', {'post': post, 'menu': menu})


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
    tags = TagPost.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'menu': menu,
        'tags': tags,
        'tagForm': TagForm

    }

    return render(request, 'blog/post_detail.html', context)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


def add_tag(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        tagForm = TagForm(request.POST)
        if tagForm.is_valid():
            tag_name = tagForm.cleaned_data['tag']
            tag_slug = slugify(tag_name)
            tag, created = TagPost.objects.get_or_create(tag=tag_name, slug=tag_slug)
            post.tags.add(tag)
            return redirect('post_detail', pk=post.pk)
    else:
        tagForm = TagForm()
    context = {
        'post': post,
        'tagForm': tagForm
    }
    return render(request, 'add_tag.html', context)


def post_by_tag(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    post = tag.tags.all()

    return render(request, 'blog/index.html', {'post': post})