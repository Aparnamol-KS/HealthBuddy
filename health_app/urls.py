from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.get_home_page,name='get_home_page'),
    path('yoga',views.get_yoga_page,name='yoga'),
    path('mental_health',views.get_mental_health_page,name='mental_health'),
    path('blog',views.blog_page,name='blog_page'),
    path('save',views.save_data,name='save'),
    path('blog_display',views.get_all_blog, name='blog_display')
]


 