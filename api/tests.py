# from django.http import response
# from mainApp.models import User
# from django.test import TestCase
# from mainApp.models import Service
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.urls import reverse

# # Create your tests here.
# class ModelTestCase(TestCase):
#     """This class defines the test suite for the Service model."""

#     def setUp(self) -> None:
#         """Define the test client and other test variables."""

#         self.email = 'avgjoe@gmail.com',
#         self.username = 'avgjoe',
#         self.full_name = 'Joe Avera',
#         self.phone_number = '7779311',
#         self.phone_ext = '+1',
#         self.latitude = 10.0,
#         self.longitude = 10.0,
#         self.is_business = False,

#         self.user = User(
#             email = self.email,
#             username = self.username,
#             full_name = self.full_name,
#             phone_number = self.phone_number,
#             phone_ext = self.phone_ext,
#             latitude = self.latitude,
#             longitude = self.longitude,
#             is_business = self.is_business
            
#         )

#         self.service_name = "Laundry"
#         self.description = ""
#         self.is_available = True
#         self.user_id = self.user
#         self.service = Service(
#             name=self.service_name,
#             description = self.description,
#             is_available = self.is_available,
#             user_id = self.user_id,
#         )

#     def test_model_can_create_a_service(self):
#         """Test the service mode can create a service."""
#         old_count = Service.objects.count()
#         self.user_id.save()
#         self.service.save()
#         new_count = Service.objects.count()
#         self.assertNotEqual(old_count, new_count)

#     def test_model_can_create_a_user(self):
#         """Test the user model can create a user."""
#         old_count = User.objects.count()
#         self.user.save()
#         new_count = User.objects.count()
#         self.assertNotEqual(old_count, new_count)

# class ViewTestCase(TestCase):
#     """Test suite for the api views."""

#     def getUser():
#         return User(
#             email = "avgjoe@gmail.com",
#             username = "avgjoe",
#             full_name = "Joe Avera",
#             phone_number = "7779311",
#             phone_ext = "+1",
#             latitude = 0.0,
#             longitude = 0.0,
#             is_business = False,
#         )

#     def setUp(self) -> None:
#         """Define the test clent and other test variables."""
#         self.client = APIClient()
#         self.user_data = {
#             'email' : 'avgjoe@gmail.com',
#             'username' : 'avgjoe',
#             'full_name' : 'Joe Avera',
#             'phone_number' : '7779311',
#             'phone_ext' : '+1',
#             'latitude' : 0.0,
#             'longitude' : 0.0,
#             'is_business' : False,
#         }
#         self.user = self.user_data
#         self.service_data = {
#             'name': 'Laundry',
#             'description': 'Expertly washed clothes, using a washing machine',
#             'is_available': True,
#             'user_id': self.user,
#         }
#         self.response = self.client.post(
#             reverse('create'),
#             self.service_data,
#             format="json"
#         )

#     def test_api_can_create_a_service(self):
#         """Test the api ha a service creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

#     def test_api_can_get_a_service(self):
#         """Test the api can get a given service."""
#         service = Service.objects.get()
#         response = self.client.get(
#             reverse('details',
#             kwargs={'pk': service.id}),
#             format="json"
#         )

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, service)

#     def createService(self):
#         return Service(
#             name = 'Laundry',
#             description = 'Expertly washed clothes, using a washing machine',
#             is_available = True,
#             user_id = self.user,
#         )

#     def test_api_can_update_service(self):
#         """Test the api can update a given service."""
#         change_service = {'name': 'newLaundry'}
#         service = Service.objects.get()
#         res = self.client.put(
#             reverse('details', kwargs={'pk': service.id}),
#             change_service,
#             format='json'
#         )

#         self.assertEqual(res.status_code, status.HTTP_200_OK)

#     def test_api_can_delete_service(self):
#         """Test the api can delete a service."""
#         service = Service.objects.get()
#         response = self.client.delete(
#             reverse('details', kwargs={'pk': service.id}),
#             format='json',
#             follow=True
#         )

#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)