from django.urls import path
from . import views

app_name = 'football_selection'

urlpatterns = [
    path('', views.selection_form, name='form'),
]
