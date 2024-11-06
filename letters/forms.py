# forms.py
from django import forms
from .models import OfferLetter, JoiningLetter, ExperienceLetter,InterviewcallLetter,PromotionLetter,SalaryincreaseLetter,TransferLetter

class OfferLetterForm(forms.ModelForm):
    class Meta:
        model = OfferLetter
        fields = ["____all______"]


class JoiningLetterForm(forms.ModelForm):
    class Meta:
        model = JoiningLetter
        fields = ["____all______"]

class ExperienceLetterForm(forms.ModelForm):
    class Meta:
        model = ExperienceLetter
        fields = ["____all______"]

class InterviewcallLetterForm(forms.ModelForm):
    class Meta:
        model = InterviewcallLetter
        fields = ["____all______"]

class PromotionLetterForm(forms.ModelForm):
    class Meta:
        model = PromotionLetter
        fields = ["____all______"]

class SalaryincreaseLetterForm(forms.ModelForm):
    class Meta:
        model = SalaryincreaseLetter
        fields = ["____all______"]

class TransferLetterForm(forms.ModelForm):
    class Meta:
        model = TransferLetter
        fields = ["____all______"]