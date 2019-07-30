from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.order_by('-date')
    context = {
        'posts' : posts, 
    }
    return render(request,'home.html',context)

