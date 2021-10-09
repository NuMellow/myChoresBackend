from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, PackageCreateView, PackageDetailsView, ReviewCreateView, ReviewDetailsView, UserCreateView, UserDetailsView, BookingCreateView, BookingDetailsView

urlpatterns = [
    path('services/', CreateView.as_view(), name="create"),
    path('services/<int:pk>/', DetailsView.as_view(), name="details"),
    path('users/', UserCreateView.as_view(), name="create"),
    path('users/<int:pk>/', UserDetailsView.as_view(), name="details"),
    path('packages/', PackageCreateView.as_view(), name="create"),
    path('packages/<int:pk>/', PackageDetailsView.as_view(), name="details"),
    path('reviews/', ReviewCreateView.as_view(), name="create"),
    path('reviews/<int:pk>/', ReviewDetailsView.as_view(), name="details"),
    path('bookings/', BookingCreateView.as_view(), name="create"),
    path('bookings/<int:pk>/', BookingDetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)