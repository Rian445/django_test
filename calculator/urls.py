
from django.urls import path
from . import views

app_name = 'calculator'  # Add this line!

urlpatterns = [

    path('', views.calculate, name='calculator'),
]
