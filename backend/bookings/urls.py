from django.urls import path
from .views import view_trains,book_trains,my_bookings,cancel_booking

urlpatterns = [
    path('trains/', view_trains, name='trains'),
    path('book/', book_trains, name='book'),
    path('my_bookings/', my_bookings, name='my_bookings'),
    path('cancel/', cancel_booking, name='cancel_booking'),

]