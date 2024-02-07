from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):

    all_posts = Post.objects.all()

    return render(request, 'base.html', {'posts' : all_posts})
