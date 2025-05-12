from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'country', 'city', 'birth_date', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'profile_picture': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'bio': 'Biography',
            'country': 'Country',
            'city': 'City',
            'birth_date': 'Birth Date',
            'profile_picture': 'Profile Picture',
        }
        help_texts = {
            'bio': 'Tell us something about yourself.',
            'country': 'Your country of residence.',
            'city': 'Your city of residence.',
            'birth_date': 'Your date of birth.',
            'profile_picture': 'Upload a profile picture.',
        }
        error_messages = {
            'bio': {
                'max_length': "This field is too long.",
            },
            'country': {
                'max_length': "This field is too long.",
            },
            'city': {
                'max_length': "This field is too long.",
            },
        }
        