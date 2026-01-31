from django.contrib import admin
from .models import Train, Booking

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        'train_no',
        'train_name',
        'source',
        'destination',
        'seats',
        'fare',
        'is_active',
        'created_at'
    )
    list_filter = ('source', 'destination', 'is_active')
    search_fields = ('train_name', 'train_no')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'train',
        'seats_booked',
        'total_fare',
        'status',
        'booked_at'
    )
    list_filter = ('status',)
