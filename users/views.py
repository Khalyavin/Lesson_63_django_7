import pytz

from datetime import datetime

from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView, TemplateView, FormView

from users.forms import CustomUserChangeForm, SignupForm, UserPasswordResetEmailForm
from users.models import User
from users.service import set_verify_token_and_send_mail, generate_password_and_send_mail


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


@method_decorator(csrf_exempt, name='dispatch')
class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('users:register_success')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            set_verify_token_and_send_mail(self.object)
        return super().form_valid(form)


class UserRegisterSuccessView(TemplateView):
    template_name = 'users/signup_success.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomUserChangeForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(csrf_exempt, name='dispatch')
def verify_email(request, token):
    current_user = User.objects.filter(verify_token=token).first()
    if current_user:
        now = datetime.now(pytz.timezone(settings.TIME_ZONE))
        if now > current_user.verify_token_expired:
            current_user.delete()
            return render(request, 'users/verify_token_expired.html')

        current_user.is_active = True
        current_user.verify_token = None
        current_user.verify_token_expired = None
        current_user.save()

        return redirect('users:login')

    return render(request, 'users/verify_failed.html')


class UserPasswordGenerateView(FormView):
    model = User
    form_class = UserPasswordResetEmailForm
    template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:reset_success')

    def form_valid(self, form):
        print(dir(form))
        if form.is_valid():
            tmp_email = form.cleaned_data["email"]
            tmp_user = User.objects.get(email=tmp_email)
            generate_password_and_send_mail(tmp_user)
            tmp_user.save()

        return super().form_valid(form)


class UserPasswordGenerateSuccessView(TemplateView):
    template_name = 'users/reset_password_ended.html'
