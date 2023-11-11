from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth.models import User

from .forms import PostForm, TagForm, CommentForm
from .models import Post, Comment, TagPost


menu = [
    {'url_name': 'syntax', 'title': 'Syntax'},
    {'url_name': 'web', 'title': 'Web'},
    {'url_name': 'ml', 'title': 'ML'},
    {'url_name': 'book', 'title': 'Book'},
]


def index(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post': page_obj,
        'menu': menu,
        'page_obj': page_obj,
    }
    return render(request, 'coolsite/index.html', context=context)


def post_list_by_topic(request, topic):
    posts = Post.objects.filter(choice=topic).order_by('-published_date')
    context = {
        'posts': posts,
        'menu': menu
    }
    return render(request, 'coolsite/post_list_by_topic.html', context)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('coolsite:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'coolsite/post_new.html', {'form': form})


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

    return render(request, 'coolsite/post_detail.html', context)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('coolsite:home')


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('coolsite:home')
    else:
        form = PostForm(instance=post)

    return render(request, 'coolsite/post_edit.html', {'form': form})


def add_tag(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        tagForm = TagForm(request.POST)
        if tagForm.is_valid():
            tag_name = tagForm.cleaned_data['tag']
            tag_slug = slugify(tag_name)
            tag, created = TagPost.objects.get_or_create(tag=tag_name, slug=tag_slug)
            post.tags.add(tag)
            return redirect('coolsite:post_detail', pk=post.pk)
    else:
        tagForm = TagForm()
    context = {
        'post': post,
        'tagForm': tagForm
    }
    return render(request, 'coolsite:add_tag.html', context)


def post_by_tag(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.all()
    context = {
        'posts': posts,
        'menu': menu
    }
    return render(request, 'coolsite/tag_post.html', context)





