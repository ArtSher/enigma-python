from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('syntax/', views.syntax, name='syntax'),
    path('web/', views.web, name='web'),
    path('ml/', views.ml, name='ml'),
    path('book/', views.book, name='book'),
    path('forum/', views.forum, name='forum'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/edit/', views.post_edit, name='post_edit'),

]