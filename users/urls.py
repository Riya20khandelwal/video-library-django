from django.urls import path 
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('add/', views.add_video, name='add_video'),
    path('videos/', views.video_list, name='video_list'),
    path('register/', views.register, name='register'),
]
