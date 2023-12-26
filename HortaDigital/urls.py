from django.urls import path
from HortaDigital.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]
