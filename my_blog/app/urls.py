from django.urls import path
from .views import Homeview, SignUpView, SignInView, MyBlogView, DeleteMyblogView, SignOutView, BlogView


urlpatterns = [
    path('', BlogView, name = "blog"), 
    path('home/', Homeview, name="home"),

    path('signup/$/', SignUpView ,name='signup'),
    path('signin/', SignInView ,name='signin'),
    path('signout/', SignOutView, name='signout'),

    path('myblog/', MyBlogView, name='myblog'), 
    path('delete/<str:pk>', DeleteMyblogView, name="delete-my-blog")
]

