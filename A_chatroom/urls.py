from django.urls import path 


from . import views


urlpatterns = [
    path('',views.index,name='index'),
    #user selects/type room name
    path('<str:name>/',views.A_room,name='A_room'),

]