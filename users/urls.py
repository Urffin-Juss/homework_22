from django.urls import path
from .views import UserCreateView, UserLogoutView, UserLoginView

app_name = 'users'

urlpatterns = [
    path('user/register/', UserCreateView.as_view(), name='register'),
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/logout/', UserLogoutView.as_view(), name='logout'),

]