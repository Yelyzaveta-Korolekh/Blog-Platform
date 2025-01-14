from django.urls import path, include
from . import views
from .views import CustomLoginView
from .views import SignupView, aboutUs, contacts, blog, addPost, editPost, postPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('about/', aboutUs, name='about_us'), 
    path('contacts/', contacts, name='contacts'),
    path('blog/', blog, name='blog'),
    path('add-post/', addPost, name='addPost'),
    path('blog/edit/<int:post_id>/', editPost, name='editPost'),
    path('blog/<int:post_id>/', postPage, name='postPage'),
]

