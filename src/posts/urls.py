from django.urls import path
from .views import index, blog, post, search, post_update, post_delete, post_create


urlpatterns = [
    path('', index),
    path('blog/', blog, name="post-list"),
    path('post/<int:id>/', post, name="post-detail"),
    path('search/', search, name='post-search'),
    path('post/create/', post_create, name="post-create"),
    path('post/<int:id>/update', post_update, name="post-update"),
    path('post/<int:id>/delete', post_delete, name="post-delete"),
]
