from django.urls import path
from .views import index, blog, post, search


urlpatterns = [
    path('', index),
    path('blog/', blog, name="post-list"),
    path('post/<int:id>/', post, name="post-detail"),
    path('search', search, name='post-search'),
]
