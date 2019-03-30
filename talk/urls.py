from django.urls import path, re_path

from talk import views

urlpatterns = [
    path('',views.index,name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]