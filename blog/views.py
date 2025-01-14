from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

def index(request): 
    posts = Post.objects.all().order_by('id')
    posts = posts[::-1]
    posts = posts[0:5]
    return render(request, 'blog/index.html', {'posts': posts})

def blog(request): 
    posts = Post.objects.all().order_by('id')
    posts = posts[::-1]
    return render(request, 'blog/blog.html', {'posts': posts})

def aboutUs(request): 
    return render(request, 'blog/aboutUs.html')

def contacts(request): 
    return render(request, 'blog/contacts.html')

class CustomLoginView(LoginView): 
    template_name = 'blog/registration/login.html'
    
    def get_success_url(self): 
        return reverse_lazy('index')

class SignupView(generic.CreateView):
    template_name = "blog/registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

def addPost(request): 
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else: 
        form = PostForm()
    return render(request, 'blog/posts/addPost.html', {'form': form})


@login_required
def editPost(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/posts/editPost.html', {'form': form, 'post': post})

def postPage (request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/posts/postPage.html', {'post' : post})

