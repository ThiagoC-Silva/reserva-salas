from django.urls import path
from . import views

urlpatterns = [
    path('criar_reserva/', views.criar_reserva, name='criar_reserva'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
]