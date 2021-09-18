from rest_framework import serializers
from mainApp.models import Service
from mainApp.models import User

class ServiceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instabce into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Service
        fields = (
            'id', 
            'name', 
            'description', 
            'images', 
            'is_available', 
            'user_id',
            'created_at',
            'modified_at'
        )
        read_only_fields = (
            'created_at',
            'modified_at'
        )