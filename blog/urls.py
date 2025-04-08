from django.contrib import admin
from django.urls import path
from blog import views as blog_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view.blog, name='blog'),
    path('<int:id>/', blog_view.post, name='post'),
]