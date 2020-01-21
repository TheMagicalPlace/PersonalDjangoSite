from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from http import server
import os
from spotipy import oauth2,SpotifyException
from urllib.parse import urlparse, parse_qs
import json
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.urls import path
class CLAAAuth(TemplateView):

    """This entire app is largely seperate from the rest of the site, and is only run
    alongside it as a matter of convenience (and to not have to buy two domain names). I am aware that
    the naming schema for a lot of this is pretty nonsensical, but honestly its more tolerable than refactoring
    everything at the moment, and since it's not like this will ever be used outside the context of the my concert
    location program its more or less harmless. Still probably the worlds worst RESTfull API, though."""

    sp_oauth = None

    def init_oauth(self,request):
        """Initializes the oauth client for spotify"""
        if self.sp_oauth is None:
            with open(os.path.join(os.getcwd(),'claa_keys.json')) as keys:
                data = json.load(keys)
                client_id = data['client_key']
                client_secret = data['client_secret']
                redirect_uri = data['redirect_uri']
            CLAAAuth.sp_oauth = oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                                           scope='playlist-read-private', cache_path=".cache-user-token")

    def get(self,request,*args):
        rootdir = os.getcwd()
        self.init_oauth(request)
        if request.path.endswith('spotify_auth_link.json'): # fun fact, this doesn't return a json file
            # HttpResponseRedirect(self.sp_oauth.get_authorize_url())
            response = HttpResponse()
            response.write(bytes(self.sp_oauth.get_authorize_url(),"utf-8"))
            return response
        elif request.path.endswith('access_token.json'):
            query_components = request.GET
            code = query_components['code']
            return self.json_get(self.sp_oauth.get_access_token(code)) # pretty sure this doesn't either

        elif request.path.endswith('.html'):
            with open(rootdir + request.path) as auth_url:
                data = request.GET
            return JsonResponse(data) # but this does.
        else:
            return HttpResponse(404)



    def json_get(self, json_file):
        """Returns a not json http response, despite the name and header"""

        response = HttpResponse()
        response.content=bytes(json.dumps(json_file), "utf-8")
        response.content_type = 'application-json'
        return response


def redirect(request,context=None):
    response = render(request,'CLAAServer/redirect.html',context)
    return response

