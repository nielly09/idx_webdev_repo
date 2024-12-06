from django.urls import path
from .views import (
    VideoListView, VideoDetailView, VideoCreateView,
    VideoUpdateView, VideoDeleteView, homepage, register_view, login_view, logout_view
)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('video list', VideoListView.as_view(), name='video_list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('video/create/', VideoCreateView.as_view(), name='video_create'),
    path('video/<int:pk>/edit/', VideoUpdateView.as_view(), name='video_update'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='video_delete'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
