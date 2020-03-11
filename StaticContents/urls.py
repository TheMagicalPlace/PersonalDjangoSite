from . import views
from django.urls import path


urlpatterns = [path('',views.index,name='index'),
               path('otherprojects/',views.otherprojects,name='otherprojects'),
                path('references/',views.references,name='references')
               ]

