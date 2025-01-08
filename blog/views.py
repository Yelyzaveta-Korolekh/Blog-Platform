from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

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
    
    def get_success_url(self): 
        return reverse_lazy('index')

class SignupView(generic.CreateView):
    template_name = "blog/registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
