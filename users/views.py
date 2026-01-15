from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser
from .form import CustomUserCreationForm, CustomUserLoginForm

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/registr.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    authentication_form = CustomUserLoginForm
    template_name = 'users/login.html'
    success_url = settings.LOGIN_REDIRECT_URL

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    success_url = settings.LOGIN_REDIRECT_URL

