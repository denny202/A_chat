from django.shortcuts import render

# Create your views here.


def index (request):
    return render(request,'iallrooms.html')


def A_room(request,name):
    return render (request,'room.html',{'name':name})