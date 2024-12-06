from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Video
from .forms import VideoForm
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Video, Comment, Heart
from .serializers import VideoSerializer, CommentSerializer, HeartSerializer, CommentCreateSerializer, HeartCreateSerializer

def register_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # Redirect if already logged in

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log in the user after registration
            return redirect('homepage')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # Redirect if already logged in

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def homepage(request):
    videos = Video.objects.all().order_by('-created_at')  # Latest videos first
    return render(request, 'homepage.html', {'videos': videos})

class VideoListView(ListView):
    model = Video
    template_name = 'video_list.html'
    context_object_name = 'videos'

class VideoDetailView(DetailView):
    model = Video
    template_name = 'video_detail.html'
    context_object_name = 'video'

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'video_form.html'
    success_url = reverse_lazy('video_list')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'video_form.html'
    success_url = reverse_lazy('video_list')

class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video_confirm_delete.html'
    success_url = reverse_lazy('video_list')

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        elif self.request.method == 'POST':
            return CommentCreateSerializer

class HeartViewSet(viewsets.ModelViewSet):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HeartSerializer
        elif self.request.method == 'POST':
            return HeartCreateSerializer
