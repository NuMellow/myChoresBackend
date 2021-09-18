from mainApp.models import User
from django.test import TestCase
from mainApp.models import Service
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class ModelTestCase(TestCase):
    """THis class defines the test suite for the Service model."""

    def setUp(self) -> None:
        """Define the test client and other test variables."""
        self.service_name = "Laundry"
        self.description = ""
        self.is_available = True
        self.user_id = User(
            email = "",
            username = "",
            full_name = "",
            phone_number = "",
            phone_ext = "",
            latitude = 0.0,
            longitude = 0.0,
            is_business = False,
        )
        self.service = Service(
            name=self.service_name,
            description = self.description,
            is_available = self.is_available,
            user_id = self.user_id,
        )

    def test_model_can_create_a_service(self):
        """Test the service mode can create a service."""
        old_count = Service.objects.count()
        self.user_id.save()
        self.service.save()
        new_count = Service.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def getUser():
        return User(
            email = "avgjoe@gmail.com",
            username = "avgjoe",
            full_name = "Joe Avera",
            phone_number = "7779311",
            phone_ext = "+1",
            latitude = 0.0,
            longitude = 0.0,
            is_business = False,
        )

    def setUp(self) -> None:
        """Define the test clent and other test variables."""
        self.client = APIClient()
        self.user = User(
            email = "avgjoe@gmail.com",
            username = "avgjoe",
            full_name = "Joe Avera",
            phone_number = "7779311",
            phone_ext = "+1",
            latitude = 0.0,
            longitude = 0.0,
            is_business = False,
        )
        self.service_data = {
            'name': 'Laundry',
            'description': 'Expertly washed clothes, using a washing machine',
            'is_available': True,
            'user_id': self.user,
        }
        self.response = self.client.post(
            reverse('create'),
            self.service_data,
            format="json"
        )

    def test_api_can_create_a_service(self):
        """Test the api ha a service creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)