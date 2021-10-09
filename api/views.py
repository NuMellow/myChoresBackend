from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .serializers import PackageSerializer, ReviewSerializer, ServiceSerializer, UserSerializer, BookingSerializer
from mainApp.models import User, Service, Package, Review, Booking

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UserCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PackageCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class PackageDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class ReviewCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BookingCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer