from django.shortcuts import render
from django.http import HttpResponse

context = {}


def index(request):
    return render(request,'StaticContents/homepage.html',context)

def otherprojects(request):
    return render(request,'StaticContents/otherprojects.html',context)
# Create your views here.
