from django.urls import path
from .views import WriteBlogView , BlogDetailView, LikeView, UpdateBlogView

urlpatterns = [
    path('write-blog/', WriteBlogView, name='write-blog'),
    path('update-blog/<str:pk>', UpdateBlogView, name='update-blog'),
    path('blogdetail/<str:pk>', BlogDetailView, name='blog-display'),
    path('blog-like/<str:pk>', LikeView, name='blog-like'),
]
