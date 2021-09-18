#from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    phone_ext = models.CharField(max_length=4)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    profile_image = models.URLField()
    is_business = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.modeified_at = timezone.now()
        self.save()

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.URLField()
    is_available = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.modeified_at = timezone.now()
        self.save()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Package(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.modeified_at = timezone.now()
        self.save()

class Booking(models.Model):
    BOOKED = "BKD"
    CANCELLED = "CND"
    STATUS_CHOICES = [
        (BOOKED, 'Booked'),
        (CANCELLED, 'Cancelled'),
    ]
    booked_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=BOOKED)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.modeified_at = timezone.now()
        self.save()

class Review(models.Model):
    ONE_STAR = 1.0
    ONE_FIVE_STAR = 1.5
    TWO_STAR = 2.0
    TWO_FIVE_STAR = 2.5
    THREE_STAR = 3.0
    THREE_FIVE_STAR = 3.5
    FOUR_STAR = 4.0
    FOUR_FIVE_STAR = 4.5
    FIVE_STAR = 5.0
    REVIEW_CHOICES = [
        (ONE_STAR, 1.0),
        (ONE_FIVE_STAR, 1.5),
        (TWO_STAR, 2.0),
        (TWO_FIVE_STAR, 2.5),
        (THREE_STAR, 3.0),
        (THREE_FIVE_STAR, 3.5),
        (FOUR_STAR, 4.0),
        (FOUR_FIVE_STAR, 4.5),
        (FIVE_STAR, 5.0),
    ]
    
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=REVIEW_CHOICES)
    review = models.TextField()
    customer_id = models.ForeignKey(User,related_name='related_customer', on_delete=models.CASCADE)
    business_id = models.ForeignKey(User, related_name='related_business', on_delete=models.CASCADE)
