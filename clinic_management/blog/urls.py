from . import views
from django.urls import path

urlpatterns = [
    path('', views.blogpage , name='blogpage'), 
    path('add-blog/', views.add_blog , name='add_blog'),
    path('post-blog/<int:edit_id>', views.post_blog , name='post_blog'),
    path('draft-blog/<int:edit_id>', views.draft_blog , name='draft_blog'),
    path('view-blog/<int:view>', views.view_blog , name='view_blog'),
]