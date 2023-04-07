from django.urls import path
from .views import Homeview, SignUpView, SignInView


urlpatterns = [
    path('', Homeview, name="home"),

    path('signup/$/', SignUpView ,name='signup'),
    path('signin/', SignInView ,name='signin'),
]

