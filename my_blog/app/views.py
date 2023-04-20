from django.shortcuts import render, redirect
from .forms import CreateUserforms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from writeblog.models import Writer, BlogWrite
from django.contrib.auth.decorators import login_required


@login_required(login_url='/signin/')
def Homeview(request):
    blog = BlogWrite.objects.all()
    context = {
        'blog' : blog,
        'name' : request.user.name,
    }
    return render(request, 'home.html', context)

def BlogView(request):
    blog = BlogWrite.objects.all()
    context = {
        'blog':blog, 
    }
    return render(request, 'blog.html', context)

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
            return redirect('signin')
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
            print(user)
            context = {
                'name': user.name,
            }
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'signin.html')
    return render(request, 'signin.html')

@login_required(login_url='/signin/')
def MyBlogView(request):
    user = request.user
    blogger = Blogger.objects.get(blogger=user)
    blog_writer = Writer.objects.get(blog_writer=blogger)
    print(blog_writer.myWrite.all())
    context = {
        'myblog': blog_writer.myWrite.all(),
        'name' : user.name,
    }

    return render(request, 'myblog.html', context)

@login_required(login_url='/signin/')
def DeleteMyblogView(request, pk):
   
    user = request.user
    blogger = Blogger.objects.get(blogger=user)
    blog_writer = Writer.objects.get(blog_writer=blogger)
    delete_blog = blog_writer.myWrite.get(id=pk)
    blog_writer.myWrite.remove(delete_blog)
    print(blog_writer.myWrite.all())
    data = BlogWrite.objects.get(id=pk)
    data.delete()

    return redirect('home')
        

@login_required(login_url='/signin/')
def SignOutView(request):
    logout(request)
    return redirect('signin')




