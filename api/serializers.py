from rest_framework import serializers
from mainApp.models import User, Service, Package

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

class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = (
            'id',
            'username',
            'full_name',
            'phone_number',
            'phone_ext',
            'latitude',
            'longitude',
            'profile_image',
            'is_business',
            'created_at',
            'modified_at'
        )

        read_only_fields = (
            'created_at',
            'modified_at'
        )

class PackageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instace into JSON format."""

    class Meta:
        model = Package
        fields = (
            'price',
            'description',
            'name',
            'is_available',
            'service_id',
            'created_at',
            'modified_at'
        )

        read_only_fields = (
            'created_at',
            'modified_at'
        )