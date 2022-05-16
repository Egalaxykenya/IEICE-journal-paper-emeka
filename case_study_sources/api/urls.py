from django.urls import path
from .views import (
        SalonDetail,
        SalonAPIView,
        SalonUserAPIView,
        UserDetailAPIView,
)

urlpatterns = [
    path('salons/', SalonAPIView.as_view()),
    path('salon/<uuid:pk>', SalonDetail.as_view()),
    path('users/', SalonUserAPIView.as_view()),
    path('user<uuid:pk>', UserDetailAPIView.as_view()),

]
