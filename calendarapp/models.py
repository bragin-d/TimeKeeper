from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Leave(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255, blank=True, null=True)  # Optional
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )
    type = models.CharField(
        max_length=20,
        choices=[
            ('sick', 'Sick Leave'),
            ('casual', 'Casual Leave'),
            ('earned', 'Earned Leave'),
            ('maternity', 'Maternity Leave'),
            ('paternity', 'Paternity Leave'),
            ('unpaid', 'Unpaid Leave'),
            ('health_day', 'Health Day'),
            ('annual_vacation', 'Annual Vacation'),
            ('study_leave', 'Study Leave')
        ],
        default='annual_vacation'
    )

    @property
    def duration(self):
        return (self.end_date - self.start_date).days + 1


class Shift(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shift_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # New automatic fields
    is_night_shift = models.BooleanField(default=False)
    is_holiday_shift = models.BooleanField(default=False)

    @property
    def duration(self):
        # Calculate the duration in hours
        duration = (datetime.combine(datetime.min, self.end_time) - datetime.combine(datetime.min, self.start_time)).seconds / 3600
        return duration

    def save(self, *args, **kwargs):
        # Check if the shift is a night shift (e.g., any shift starting after 10 PM or ending before 6 AM)
        self.is_night_shift = self.start_time >= time(22, 0) or self.end_time <= time(6, 0)
        
        # You can also check if the shift is a holiday shift by comparing the shift date to a list of holiday dates.
        # Here's a basic example with a holiday date list (you can replace this with your actual holiday logic)
        holiday_dates = ['2024-12-25', '2024-01-01']  # Example: Christmas and New Year's Day
        self.is_holiday_shift = str(self.shift_date) in holiday_dates

        super().save(*args, **kwargs)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.event_date}"