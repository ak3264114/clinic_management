from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name


class Blog(models.Model):
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=20)
    blog_image = models.ImageField(upload_to = 'asset/blog_image')
    blog_summary = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_views = models.IntegerField(default=0)
    blog_is_post = models.BooleanField(default=False)
    def __str__(self):
        return self.blog_title