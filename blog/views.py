from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse


def blog(request,context=None):
    context = {'posts':Post.objects.all()}
    return render(request, 'blog/blog.html', context)