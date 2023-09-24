from django.urls import re_path
from . import consumers
#more advanced paths

websocket_urlpatterns= [
    #capture name of room 

    #w+ anything chat slash it will be passed to consumer 
    #match any word
    #/$ end the path 
    re_path(r'ws/chat/(?P<name>\w+)/$',consumers.cons_room),
]