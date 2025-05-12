from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .utils import validate_unique_username

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(validators=[validate_unique_username])
    terms_and_conditions = forms.BooleanField(
        required=True,
        label="Accept Terms and Conditions",
        error_messages={
            'required': 'You must accept the terms and conditions to register.'
        },
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "terms_and_conditions")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user
