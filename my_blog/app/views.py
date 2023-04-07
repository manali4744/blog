from django.shortcuts import render, redirect
from .forms import CreateUserforms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from writeblog.models import Writer, BlogWrite

def Homeview(request):
    blog = BlogWrite.objects.all()
    context = {
        'blog' : blog,
    }
    return render(request, 'home.html', context)

def SignUpView(request):
    form = CreateUserforms()
    if request.method == "POST":
        form = CreateUserforms(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            messages.success(request, 'Account was created for ' + username)
            blogger= Blogger.objects.create(blogger=user)
            writer = Writer.objects.create(blog_writer=blogger)
            return redirect('home')
    context = {'form': form}
    return render(request, 'signup.html', context)

def SignInView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print(email)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'signin.html')
    return render(request, 'signin.html')



