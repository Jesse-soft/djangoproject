from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("room_page/<int:pk>/",views.room, name="room"),
]