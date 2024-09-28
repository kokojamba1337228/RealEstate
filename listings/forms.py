from django import forms
from django.contrib.auth.models import User
from .models import Property

class SignUpForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text="Enter your phone number.")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class PropertyAddForm(forms.ModelForm):
    #phone_number = forms.CharField(max_length=13, required=True, help_text="Enter your phone number.")

    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'user']

    def save(self, commit=True):
        property = super(PropertyAddForm, self).save(commit=False)
        if commit:
            property.save()
        return property