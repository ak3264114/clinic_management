from urllib import request
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blog.models import Blog, Category
# Create your views here.

def blogpage(request):
    if Blog.objects.filter(blog_is_post=True).exists():
        contents = Blog.objects.filter(blog_is_post=True)
        return render(request, "home.html", {"contents":contents})
    else:
        return render(request, "home.html")
def add_blog(request):
    if request.user.is_staff :
        if request.method == "POST":
            blog_author = request.user
            blog_image =request.FILES['blog_image']
            blog_category = request.POST['blog_category']
            blog_title = request.POST['blog_title']
            blog_summary = request.POST['blog_summary']
            blog_content = request.POST['blog_content']
            if "draft_blog" in request.POST:
                Blog(blog_author=blog_author, blog_title=blog_title, blog_category_id=blog_category, blog_image=blog_image, blog_summary=blog_summary, blog_content=blog_content, blog_is_post = False).save()
                messages.success(request, "your blog is successfully saved as draft")
                return redirect('add_blog')
            elif "post_blog" in request.POST:
                Blog(blog_author=blog_author, blog_title=blog_title, blog_category_id=blog_category, blog_image=blog_image, blog_summary=blog_summary, blog_content=blog_content, blog_is_post = True).save()
                messages.success(request, "your blog is successfully Post")
                return redirect('add_blog')
            else:
                return HttpResponse ("An error occoured please try again")      
        else:
            categorys = Category.objects.all
            return render(request, "add_blog.html", {"categorys": categorys})
    else:
        return redirect('blogpage')

# def edit_blog(request, edit_id):
#     if request.user.is_staff and ((Blog.objects.get(id = edit_id).blog_author) ==  request.user):
#         content = Blog.objects.get(id = edit_id)
#         categorys = Category.objects.all
#         return render(request, "edit_blog.html", {"content": content , "categorys":categorys})
#     else :
#         return HttpResponse("fail")

def post_blog(request, edit_id):
    Blog.objects.filter(id = edit_id).update(blog_is_post=True)
    messages.success(request, "Your details has been Post succesfully!")
    return redirect("profile")


def draft_blog(request, edit_id):
    Blog.objects.filter(id = edit_id).update(blog_is_post=False)
    messages.success(request, "Your details has been Saved as Draft succesfully!")
    return redirect("profile")

def view_blog(request, view):
    Blog.objects.filter(id = view).update(blog_views =Blog.objects.get(id=view).blog_views + 1)
    content = Blog.objects.get(pk=view)
    return render(request, "blog.html" , {"content":content})