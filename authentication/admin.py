from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Fields displayed in the admin list view
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'job_title', 'phone_number')

    # Fields displayed on the edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone_number','holiday_days_remaining','health_days_remaining','is_on_vacation','job_title',)}),  # Custom field for editing
    )
    
    # Fields displayed on the creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('phone_number','holiday_days_remaining','health_days_remaining','is_on_vacation','job_title',)}),  # Custom field for creation
    )