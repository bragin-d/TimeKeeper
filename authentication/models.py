from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    holiday_days_remaining = models.IntegerField(default=0)
    health_days_remaining = models.IntegerField(default=0)
    is_on_vacation = models.BooleanField(default=False)
    job_title = models.CharField(max_length=30, blank=True, null=True)
