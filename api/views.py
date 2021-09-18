from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .serializers import ServiceSerializer
from mainApp.models import Service
from mainApp.models import User

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