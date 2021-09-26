from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserCreateView, UserDetailsView

urlpatterns = [
    path('services/', CreateView.as_view(), name="create"),
    path('services/<int:pk>/', DetailsView.as_view(), name="details"),
    path('users/', UserCreateView.as_view(), name="create"),
    path('users/<int:pk>/', UserDetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)