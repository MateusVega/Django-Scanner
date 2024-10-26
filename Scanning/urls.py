from django.urls import path
from . import views

urlpatterns = [
    path('', views.scanning, name='scanning'),
    path('save_qr_data/', views.save_qr_data, name='save_qr_data')
]
