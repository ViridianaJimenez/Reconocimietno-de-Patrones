from django.urls import path
from .views import sintactico

#app_name = 'sintactico'

urlpatterns = [
    path('sintactico/', sintactico, name="sintactico")
]