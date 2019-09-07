# -*- encoding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=20,
                               error_messages={
                                   'required': '用户名不能为空',
                                   'min_length': '用户名最少为 8 位',
                                   'max_length': '用户名最多为 20 位',
                               })
    password = forms.CharField(required=True, min_length=8, max_length=20,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码最少为 8 位',
                                   'max_length': '密码最多为 20 位',
                               })


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPasswordForm(forms.Form):
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

