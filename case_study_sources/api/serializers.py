from django.contrib.auth import get_user_model
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
    ServiceCategory,
)


class UserSerializer(serializers.ModelSerializer):
    model = get_user_model()
    fields = (
        'id',
        'username',
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

class SalonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonUser
        fields = (
            'username',
            'email',
            'phone_number',
            'date_of_birth',
            'nationality',
            'city',
        )

class SalonServiceCategory(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = (
            'owner',
            'category_name',
            'created',
        )

class SalonServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SalonService
        fields = (
            'service_name',
            'owner',
            'service_category',
            'linked_business',
            'service_price',
            'service_duration',
        )

class SalonStylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonStylist
        fields = (
            'owner',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'salon_services',
            'salon',
            'working_days',
            'created',

        )

class SalonOperationDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonOperationDays
        fields = (
            'owner',
            'linked_business',
            'day_of_week',
            'start_time',
            'end_time',
            'created',
        )


class SalonCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonCustomer
        fields = (
            'first_name',
            'last_name',
            'gender',
            'registered_by',
            'salon_branch',
            'created',
        )

class SalonOnsiteBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonOnsiteBooking
        fields = (
            'booked_service',
            'salon_customer',
            'booked_in_by',
            'creation_date',
            'service_date',
            'service_started',
            'service_completed',
            'service_cancelled',
            'cancellation_reason',
            'stylists',
            'negotiate_service_price',
        )

class SalonOnsiteBookingPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonOnsiteBookingPayment
        fields = (
            'salon',
            'payment_received_by',
            'payment_for',
            'payment_option',
            'payment_code',
            'payment_date',
        )