from django.urls import path
from .migrations import views

urlpatterns = [
    path('blogs/', views.blog_list_create, name='blog-list-create'),
]
