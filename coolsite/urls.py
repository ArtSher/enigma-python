from django.urls import path
from django.views.generic import ListView

from . import views

app_name = 'coolsite'
urlpatterns = [
    path('', views.index, name='home'),
    path('forum/', views.forum, name='forum'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/add/', views.add_tag, name='add_tag'),
    path('post/tag/<slug:tag_slug>/', views.post_by_tag, name='post_by_tag'),
    path('/<str:topic>/', views.post_list_by_topic, name="post_list_by_topic"),

]