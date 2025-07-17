from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('calculator/', include('calculator.urls')),
    path('football/', include('football_selection.urls')),
    path('rps/', include('rps_game.urls')),
    path('', include('main.urls')),
]
