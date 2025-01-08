from django.shortcuts import render 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def index(request): 
    return render(request, 'blog/index.html')

def aboutUs(request): 
    return render(request, 'blog/aboutUs.html')

def contacts(request): 
    return render(request, 'blog/contacts.html')

def blog(request): 
    return render(request, 'blog/blog.html')

class CustomLoginView(LoginView): 
    template_name = 'blog/registration/login.html'

class SignupView(generic.CreateView):
    template_name = "blog/registration/signup.html"
    form_class = UserCreationForm