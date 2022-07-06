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
    owner = UserSerializer()

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
    owner = UserSerializer()
    
    class Meta:
        model = ServiceCategory
        fields = (
            'owner',
            'category_name',
            'created',
        )

class SalonServiceSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    service_category = SalonServiceCategory()
    
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

class SalonOperationDaysSerializer(serializers.ModelSerializer):
    linked_business = SalonSerializer()
    
    class Meta:
        model = SalonOperationDays
        fields = (
            'linked_business',
            'day_of_week',
            'start_time',
            'end_time',
        )



class SalonStylistSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    salon_services = SalonServiceSerializer()
    working_days = SalonOperationDaysSerializer()
    
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
    owner = UserSerializer()
    linked_business = SalonSerializer()
    
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
    registered_by = UserSerializer()
    salon_branch = SalonSerializer()
    
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
    stylists = SalonStylistSerializer()
    booked_service = SalonServiceSerializer()
    booked_in_by = UserSerializer()
    salon_customer = SalonCustomerSerializer()
    
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
    salon = SalonSerializer()

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