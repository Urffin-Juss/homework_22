from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ("username", "email", "country", "city", "image", "phone")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            send_mail(
                subject="Welcome to market",
                message="Thank you for registering",
                from_email='admin@techmarket.com',
                recipient_list=[user.email],
                fail_silently=True,



            )
        return user


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)