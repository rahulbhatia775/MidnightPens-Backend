from django.urls import path
from blogapp import views


urlpatterns = [
    path('blogs/', views.blog_list_create, name='blog-list-create'),
]
