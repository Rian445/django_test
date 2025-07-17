from django.urls import path
from . import views

app_name = 'football_selection'  # Define namespace for the app

urlpatterns = [
    path('', views.selection_form, name='form'),  # Form at /football/
]
