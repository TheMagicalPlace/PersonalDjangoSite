from . import views
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse


urlpatterns = [path('access_token_auth', views.CLAAAuth.as_view(), name='claa_auth'),
               path('access_token_auth/spotify_auth_link.json', views.CLAAAuth.as_view(), name='claa_1'),
               path('access_token_auth/access_token.json', views.CLAAAuth.as_view(), name='claa_2'),
               path('access_token_auth/redirect.html',views.redirect,name='redirect')]

