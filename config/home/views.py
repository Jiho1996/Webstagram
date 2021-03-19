from django.shortcuts import render
from .forms import createPost

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def board(request):
    return render(request,'home/board.html')
 
def createPost(request):
    form = CreatePost()
 
    return render(request, 'createPost.html', {'form': form})