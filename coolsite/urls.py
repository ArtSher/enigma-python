from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('syntax/', views.syntax, name='syntax'),
    path('web/', views.web, name='web'),
    path('ml/', views.ml, name='ml'),
    path('book/', views.book, name='book'),
    path('forum/', views.forum, name='forum'),
]