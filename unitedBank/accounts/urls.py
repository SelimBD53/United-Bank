from django.urls import path

from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
]
