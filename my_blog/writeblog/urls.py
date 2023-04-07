from django.urls import path
from .views import WriteBlogView , BlogDetailView

urlpatterns = [
    path('write-blog/', WriteBlogView, name='write-blog'),
    path('blogdetail/<str:pk>', BlogDetailView, name='blog-display'),
]
