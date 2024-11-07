from django.urls import path
from . import views
from .views import off_letter_view

urlpatterns = [
    path('joining-letter/', joining_letter_view, name='join_letter'),
    path('experience-letter/', experience_letter_view, name='experience_letter'),
    path('interview-call/', interviewcall_letter_view, name='interviewcall_letter'),
    path('promotion-letter/', promotion_letter_view, name='promotion_letter'),
    path('salary-increase-letter/', salary_increase_letter_view, name='salaryincrease_letter'), 
    path('transfer-letter/', transfer_letter_view, name='transfer_letter'),
    path('leave-approval/', leave_approval_view, name='leaveapproval_letter'),
    path('resignation/', resignation_letter_view, name='resignation_letter'),
    path('termination/',termination_letter_view, name='termination_letter'),
    path('separation-agreement/', separation_letter_view, name='separation_letter'),
    path('warning-letter/', warning_letter_view, name='warning_letter'),
    path('performance-letter/', performance_letter_view, name='performance_letter'),
    path('reference-letter/', reference_letter_view, name='reference_letter'),
    path('off_letter/', off_letter_view, name='off_letter')

   
]


