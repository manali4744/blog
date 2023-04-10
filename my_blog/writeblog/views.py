from django.shortcuts import render, redirect
# from .models import Write
from django.contrib.auth.decorators import login_required
from .forms import BlogWriteForm
from app.models import Blogger
from .models import Writer, BlogWrite
# Create your views here.


@login_required(login_url='/signin/')
def WriteBlogView(request):
    form = BlogWriteForm()
    if request.method == 'POST':
        form = BlogWriteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = form.cleaned_data.get('title')
            print(data)
            blog = BlogWrite.objects.get(title=data)
            blogger = Blogger.objects.get(blogger=request.user)
            writer = Writer.objects.get(blog_writer=blogger)
            writer.myWrite.add(blog.id)
            print(writer.myWrite.all())
            return redirect('home')
    context={'form':form}
    return render(request, 'write_blog.html', context)

@login_required(login_url='/signin/')
def UpdateBlogView(request, pk):
    form = BlogWriteForm()
    writeblog = BlogWrite.objects.get(id=pk)
    form = BlogWriteForm(initial={'title': writeblog.title, 'description':writeblog.description, 'blog_img':writeblog.blog_img})
    if request.method == 'POST':
        form = BlogWriteForm(request.POST, request.FILES, instance=writeblog)
        if form.is_valid():
            form.save()
           
            return redirect('home')
    context={'form': form}
    return render(request, 'write_blog.html', context)

def BlogDetailView(request,pk):
    blog = BlogWrite.objects.get(id=pk)
    context={
        'blog': blog
    }
    return render(request, 'blog_display.html', context)

@login_required(login_url='/signin/')
def LikeView(request, pk):
    user= request.user
    blog = BlogWrite.objects.get(id=pk)
    # print(blog.like.all())
    # print("before")
    if user in blog.like.all():
        blog.like.remove(user)
        blog.save()
        # print(blog.like.all())
    else:
        blog.like.add(user)  
        blog.save()
    # print("after")
    # print(blog.like.all().count())
    return redirect('home')