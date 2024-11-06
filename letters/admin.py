from django.contrib import admin
from .models import OfferLetter

class OfferLetterAdmin(admin.ModelAdmin):
    list_display = (
        'salutation', 'name', 'email_id', 'mobile', 'dob', 
        'address', 'position', 'salary', 'start_date', 
        'working_hours', 'probation_period', 'company_name', 
        'report_manager', 'manager_name', 'department_name', 
        'benefits', 'acceptance_deadline'
    )

admin.site.register(OfferLetter, OfferLetterAdmin)
