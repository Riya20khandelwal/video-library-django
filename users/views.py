from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# View to upload or add video
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form})

# View to display the list of videos
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


# Create your views here.
def index(request):

    return render(request,'index.html')