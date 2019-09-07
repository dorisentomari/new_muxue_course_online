from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.views.generic import View
from django.urls import reverse

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetPasswordForm, ModifyPasswordForm
from apps.utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户登录
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
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
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {
                    'login_form': login_form,
                    'msg': '用户名或密码错误'
                })


# 用户退出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


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
            user_profile.is_active = False
            user_profile.save()

            send_register_email(username, 'register')

            return render(request, 'login.html', {})


class ActiveUserView(View):
    def get(self, request, active_code):
        record = EmailVerifyRecord.objects.filter(code=active_code).first()
        if record:
            email = record.email
            user = UserProfile.objects.get(email=email)
            user.is_active = True
            user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'active.html')


class ForgetPasswordView(View):
    def get(self, request):
        forget_form = ForgetPasswordForm()
        return render(request, 'forgetpwd.html', {
            'forget_form': forget_form
        })

    def post(self, request):
        forget_form = ForgetPasswordForm(request.POST)
        if forget_form.is_valid() is not True:
            return render(request, 'forgetpwd.html', {
                'forget_form': forget_form
            })
        email = request.POST.get('email', '')
        send_register_email(email, 'forget')
        return render(request, 'send_success.html')


class ResetView(View):
    def get(self, request, active_code):
        record = EmailVerifyRecord.objects.filter(code=active_code).first()
        print(record)
        if record:
            if record.is_delete is True:
                print('msg', '验证码已失效')
                return render(request, 'password_reset.html', {
                    'active_code': active_code,
                    'msg': '验证码已失效',
                    'is_expire': True
                })
            else:
                email = record.email
                print('email', email)
                return render(request, 'password_reset.html', {
                    'email': email,
                    'active_code': active_code,
                })
        else:
            return render(request, 'active.html')


class ModifyView(View):
    def post(self, request):
        modify_form = ModifyPasswordForm(request.POST)
        email = request.POST.get('email', '')
        active_code = request.POST.get('active_code', '')

        if modify_form.is_valid() is not True:
            return render(request, 'password_reset.html', {
                'email': email,
                'modify_form': modify_form
            })

        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            return render(request, 'password_reset.html', {
                'email': email,
                'msg': '两次输入的密码不一致'
            })

        user = UserProfile.objects.filter(email=email).first()
        user.password = make_password(password1)
        user.save()
        record = EmailVerifyRecord.objects.filter(code=active_code)
        if record:
            record = record.first()
            record.is_delete = True
            record.save()
        return render(request, 'login.html')
