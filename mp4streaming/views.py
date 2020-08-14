from django.shortcuts import render
from DjangoBase.settings import MEDIA_URL
# Create your views here.
def mp4(request):
    print(MEDIA_URL)
    return render(request,'mp4streaming/mp4.html',{'media': MEDIA_URL})