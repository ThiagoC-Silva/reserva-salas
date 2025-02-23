from django.urls import path
from . import views

urlpatterns = [
    path('criar_reserva/', views.criar_reserva, name='criar_reserva'),
]