import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserType(models.Model):
    is_salon_owner = models.BooleanField(default=False)
    is_salon_customer = models.BooleanField(default=False)

    class Meta:
        abstract = True

class SalonUser(AbstractUser, UserType):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=14)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.username


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        abstract = True

class Salon(Address):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="salons_owned")
    business_name = models.CharField(max_length=100)
    business_phone_number = models.CharField(max_length=15)
    business_email = models.EmailField()
    price_range = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.business_name

class BioDescription(models.Model):
    bio_description = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

class SalonCustomer(BioDescription, Address):
    GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('NM', 'Non Binary'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=GENDER, default='Male', help_text="Select gender")
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="registered_customers")
    salon_branch = models.ForeignKey(Salon, on_delete=models.PROTECT, related_name="registered_salon")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{}-{}".format(self.first_name, self.last_name)


class CategoryDescription(models.Model):
    category_description = models.CharField(max_length=255)

    class Meta:
        abstract = True

class ServiceCategory(CategoryDescription):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="service_categories")
    category_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.category_name

class SalonService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_salon_services")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT, related_name="category_services")
    linked_business = models.ForeignKey(Salon, on_delete=models.PROTECT, related_name="salon_services")
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_duration = models.DurationField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.service_name

class SalonOperationDays(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_operation_days")
    linked_business = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="salon_operation_days")
    day_of_week = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_stime = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.day_of_week

class SalonStylist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="my_salon_stylists")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    salon_services = models.ForeignKey(SalonService, on_delete=models.PROTECT, related_name="assigned_stylists")
    salon = models.ForeignKey(Salon, on_delete=models.PROTECT, related_name="salon_stylists")
    working_days = models.ForeignKey(SalonOperationDays, on_delete=models.PROTECT, related_name="stylists_assigned")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{}-{}".format(self.first_name, self.last_name)


class CancellationReason(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="my_salon_cancellation_reasons")
    cancellation_reason = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added_date',)

    def __str__(self):
        return self.cancellation_reason

class SalonOnsiteBooking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booked_service = models.ForeignKey(SalonService, on_delete=models.PROTECT, related_name="service_bookings")
    salon_customer = models.ForeignKey(SalonCustomer, on_delete=models.PROTECT, related_name="customer_bookings")
    booked_in_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="booked_customers")
    creation_date = models.DateTimeField(auto_now_add=True)
    service_date = models.DateTimeField()
    service_started = models.BooleanField(default=False)
    service_completed = models.BooleanField(default=False)
    service_cancelled = models.BooleanField(default=False)
    cancellation_reason = models.ForeignKey(CancellationReason, on_delete=models.PROTECT, related_name="cancellation_reasons_bookings", blank=True)
    multiple_stylists_assigned = models.BooleanField(default=False)
    stylists = models.ManyToManyField(SalonStylist)
    negotiate_service_price = models.BooleanField(default=False)
    negotiated_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return self.booked_service.service_name


class SalonOnsiteBookingPayment(models.Model):
    PAYMENTOPTIONS = (
    ('C', 'Cash'),
    ('M', 'Mobile'),
    ('CD', 'Card'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="salon_payments")
    payment_received_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    payment_for = models.OneToOneField(SalonOnsiteBooking, on_delete=models.PROTECT)
    payment_option = models.CharField(max_length=2, choices=PAYMENTOPTIONS)
    payment_code = models.CharField(max_length=10, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-payment_date',)

    def __str__(self):
        return "{}-{}".format(self.payment_for.service_name, self.payment_for.service_price)
