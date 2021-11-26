from django.shortcuts import render
from rest_framework import generics, permissions
from main_app.models import (
    SalonUser,
    Salon,
    SalonCustomer,
    SalonService,
    SalonStylist,
    SalonOnsiteBooking,
    SalonOnsiteBookingPayment,
    SalonOperationDays,
)

from .serializers import (
    SalonSerializer,
    )


class SalonAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class SalonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
