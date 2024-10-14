from django.shortcuts import render, HttpResponse

# Create your views here.
rooms=[
    {'id':1,'name':'lets learn python'},
    {'id':2, 'name':'design with me'},
    {'id':3, 'name':'frontend developers'}, 
       ]

def home(request):
    context = {'rooms':rooms}
    return render(request, "home.html",context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id']== pk:
            room=i
    context = {'room':room}
    return render(request, "room.html",context)
