from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
