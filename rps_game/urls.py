from django.urls import path
from . import views

app_name = 'rps_game'

urlpatterns = [
    path('', views.play_rps, name='play'),
]
