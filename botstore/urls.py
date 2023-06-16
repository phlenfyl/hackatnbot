from django.urls import path


from . views import *


app_name = 'botstore'


urlpatterns =[
    path('', home, name='home'),
    path('chat', chatresponseAPI, name='chatresponseAPI'),
]