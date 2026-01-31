from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Train,Booking
from .serializers import TrainSerializer,BookingSerializer

# Create your views here.
@api_view(['GET'])
def view_trains(request):
    trains = Train.objects.filter(is_active=True)
    serializer = TrainSerializer(trains, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def book_trains(request):
    train_id = request.data.get('train_id')
    seats = int(request.data.get('seats'))

    train = get_object_or_404(Train, id=train_id, is_active=True)

    if train.seats < seats:
        return Response(
            {"error":"Not enough seats available"},
            status=400
        )

    train.seats -= seats
    train.save()

    booking = Booking.objects.create(
        user=User.objects.first(),
        train=train,
        seats_booked=seats,
        total_fare = seats*train.fare
    )

    serializer = BookingSerializer(booking)
    return Response(serializer.data,status=201)

@api_view(['GET'])
@permission_classes([AllowAny])
def my_bookings(request):
    bookings = Booking.objects.filter(user=User.objects.first()).select_related('train')

    data = []
    for booking in bookings:
        data.append({
            'id': booking.id,
            'train_name': booking.train.train_name,
            'source': booking.train.source,
            'destination': booking.train.destination,
            'seats_booked': booking.seats_booked,
            'total_fare': booking.total_fare,
            'status': booking.status,
            'booked_at': booking.booked_at,
        })

    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def cancel_booking(request):
    booking_id = request.data.get('booking_id')

    booking = get_object_or_404(Booking, id=booking_id,user=User.objects.first(),status='BOOKED')
    train = booking.train

    train.seats += booking.seats_booked
    train.save()

    booking.status = 'CANCELLED'
    booking.save()

    return Response({"message":"Booking canceled successfully"})

