from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic import View

from .models import UserProfile
from .forms import LoginForm, RegisterForm
from apps.utils.email_send import send_register_email

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid() is not True:
            return render(request, 'login.html', {
                'login_form': login_form
            })
        else:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {
                    'login_form': login_form
                })


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid() is not True:
            return render(request, 'register.html', {
                'register_form': register_form
            })
        else:
            username = request.POST.get('email', '')
            if UserProfile.objects.filter(email=username):
                return render(request, 'register.html', {
                    'msg': '用户已存在',
                    'register_form': register_form
                })
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = username
            user_profile.password = make_password(password)
            user_profile.is_active = True
            user_profile.save()

            send_register_email(username, 'register')

            return render(request, 'login.html', {})
