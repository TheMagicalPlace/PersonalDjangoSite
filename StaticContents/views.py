from django.shortcuts import render
from django.http import HttpResponse

posts =\
[
    {
    'nice': 'n',
    'mean' : 'y',
    'tttt' : 234234
    },
    {
        'nice': 'ns',
        'mean': 'ys2',
        'tttt': 23421234
    }

]

def index(request):
    context = {'posts':posts}
    return render(request,'StaticContents/homepage.html',context)
# Create your views here.
