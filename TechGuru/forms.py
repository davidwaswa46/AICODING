from django import forms
from .models import Enrollment  # Create an Enrollment model to store enrollment data

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['name', 'email', 'course']  # Ensure these match your form fields
