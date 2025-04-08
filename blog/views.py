from django.shortcuts import render
from blog.data import posts

# Create your views here.
def blog(request):
    context = {
        'title': 'Blog',
        'posts': posts,
    }

    return render(
        request, 
        'blog/index.html',
        context=context,
    )

def post(request, id):
    context = {
        'title': 'Post',
        'posts': posts,
    }

    return render(
        request, 
        'blog/index.html',
        context=context,
    )