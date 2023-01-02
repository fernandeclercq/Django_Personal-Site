from posts.models import Post

def context_processor(request):

    latest_list = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'latest_post_list': latest_list,
    }
    return context   