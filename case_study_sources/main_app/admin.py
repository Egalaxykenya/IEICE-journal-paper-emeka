from django.contrib import admin
from .models import (
    SalonUser,
    Salon,
    SalonCustomer,
    SalonService,
    SalonStylist,
    SalonOperationDays,
    SalonOnsiteBooking,
    SalonOnsiteBookingPayment,
    ServiceCategory,
    CancellationReason,
    )

admin.site.register(SalonUser)
admin.site.register(Salon)
admin.site.register(SalonCustomer)
admin.site.register(SalonStylist)
admin.site.register(SalonOperationDays)
admin.site.register(SalonOnsiteBooking)
admin.site.register(SalonOnsiteBookingPayment)
admin.site.register(SalonService)
admin.site.register(ServiceCategory)
admin.site.register(CancellationReason)
