from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions 
from main_app.permissions import IsOwnerOrReadonly
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
    SalonUserSerializer,
    SalonCustomerSerializer,
    SalonServiceSerializer,
    SalonStylistSerializer,
    SalonOnsiteBookingSerializer,
    SalonOnsiteBookingPaymentSerializer,
    SalonOperationDaysSerializer,
    UserSerializer,

    )

class SalonAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class SalonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class SalonUserAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonUser.objects.all()
    serializer_class = SalonUserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SalonCustomerAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonCustomer.objects.all()
    serializer_class = SalonCustomerSerializer

class SalonServiceAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonService.objects.all()
    serializer_class = SalonServiceSerializer

class SalonStylistAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonStylist.objects.all()
    serializer_class = SalonStylistSerializer

class SalonOnsiteBookingAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonOnsiteBooking.objects.all()
    serializer_class = SalonOnsiteBookingSerializer

class SalonOnsiteBookingPaymentsAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonOnsiteBookingPayment.objects.all()
    serializer_class = SalonOnsiteBookingPaymentSerializer

class SalonOperationDaysAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadonly)
    queryset = SalonOperationDays.objects.all()
    serializer_class = SalonOperationDaysSerializer