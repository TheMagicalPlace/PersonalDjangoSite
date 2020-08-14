from . import views
from django.urls import path


urlpatterns = [path('mp4streaming/',views.mp4,name='mp4')]
