from django.contrib import admin
from blog import models

from blog.models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_image','blog_category', 'blog_summary', 'blog_content')




admin.site.register(Category)
admin.site.register(Blog ,  BlogAdmin)