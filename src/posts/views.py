from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.shortcuts import render, get_object_or_404
from .models import Post
from marketing.models import Signup
from django.db.models import Count, Q


def get_categories_count():
    all_categories = Post.objects.values('categories__title').annotate(Count('categories'))
    return all_categories


def search(request):
    posts = Post.objects.all()
    
    query = request.GET.get('search-item')
    if query:
        filtered_posts = posts.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'filtered_posts': filtered_posts,
    }
    
    return render(request, 'search_results.html', context)
    pass


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
    category_count = get_categories_count()
    posts = Post.objects.all()
    most_recent_posts = Post.objects.order_by('-timestamp')[0:3]
    paginator = Paginator(posts, 2)
    page_request = 'page'
    page = request.GET.get('page')

    try:
        paginated = paginator.page(page)
    
    except PageNotAnInteger:
        paginated = paginator.page(1)
    except EmptyPage:
        paginated = paginator.page(paginator.num_pages)

    context = {
        'paginated_set': paginated,
        'most_recent_posts': most_recent_posts,
        'page': page_request,
        'category_list': category_count,
    }



    return render(request, 'blog.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    category_count = get_categories_count()
    most_recent_posts = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'post': post,
        'category_list': category_count,
        'most_recent_posts': most_recent_posts,
    }
    return render(request, 'post.html', context)


