from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.models import (
    SalonUser,
    Salon,
    SalonService,
    SalonCustomer,
    SalonStylist,
    SalonOperationDays,
    SalonOnsiteBooking,
    SalonOnsiteBookingPayment,
)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerSalonEditMixin(LoginRequiredMixin, OwnerMixin):
    model = Salon
