from django.urls import path
from .views import SalonAPIView

urlpatterns = [
    path('', SalonAPIView.as_view()),
]
