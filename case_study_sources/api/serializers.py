from rest_framework import serializers
from main_app.models import (
    SalonUser,
    Salon,
    SalonService,
    SalonStylist,
    SalonCustomer,
    SalonOnsiteBooking,
    SalonOnsiteBookingPayment,
    SalonOperationDays,
)

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = (
            'id',
            'owner',
            'business_name',
            'business_phone_number',
            'business_email',
            'price_range',
            'country',
            'city',
            'region',
            'postal_code',
            'street',
            'latitude',
            'longitude',
        )
