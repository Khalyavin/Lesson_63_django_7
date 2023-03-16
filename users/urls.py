from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLoginView, UserRegisterView, UserUpdateView, UserRegisterSuccessView, \
    verify_email, UserPasswordGenerateView, UserPasswordGenerateSuccessView

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password/', PasswordChangeView.as_view(success_url='/'), name='password'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/success/', UserRegisterSuccessView.as_view(), name='register_success'),

    path('reset_password/', UserPasswordGenerateView.as_view(), name='reset_password'),
    path('reset_password_success/', UserPasswordGenerateSuccessView.as_view(), name='reset_success'),

    path('update/ ', UserUpdateView.as_view(), name='profile'),

    path('verify/<str:token>/', verify_email, name='verify_email'),

]
