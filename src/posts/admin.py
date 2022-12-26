from django.contrib import admin
from .models import Category, Post, Author

# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)


