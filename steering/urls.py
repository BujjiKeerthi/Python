from django.urls import path
from .views import predict_steering

urlpatterns = [
    path('predict/', predict_steering, name='predict_steering'),
]
