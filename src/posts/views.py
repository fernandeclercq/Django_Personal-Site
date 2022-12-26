from django.shortcuts import render
from .models import Post
from marketing.models import Signup


def index(request):
    posts = Post.objects.filter(featured=True)
    latest_list = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'post_lists': posts,
        'latest_list': latest_list,
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html', {})


def post(request):
    return render(request, 'post.html', {})


