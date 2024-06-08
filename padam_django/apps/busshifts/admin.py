from django.contrib import admin
from . import models
from .models import BusShift, BusStop


class BusStopInline(admin.TabularInline):
    model = BusStop
    extra = 1

@admin.register(BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    inlines = [BusStopInline]
    list_display = ('id', 'bus', 'driver', 'start_time', 'end_time')

@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift', 'order', 'arrival_time')
