from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.views.generic import View
from django.urls import reverse

from pure_pagination import Paginator, PageNotAnInteger

from .forms import LoginForm, RegisterForm, ForgetPasswordForm, ModifyPasswordForm
from users.forms import UserInfoForm, ChangePwdForm, UploadImageForm
from users.forms import RegisterGetForm, UpdateMobileForm
from apps.utils.email_send import send_register_email

from operation.models import UserFavorite, UserMessage
from organization.models import CourseOrg, Teacher
from courses.models import Course
from .models import UserProfile, EmailVerifyRecord


def message_nums(request):
    if request.user.is_authenticated:
        return {'unread_nums': request.user.usermessage_set.filter(has_read=False).count()}
    else:
        return {}


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
            return HttpResponseRedirect(reverse('index'))
        next = request.GET.get('next', '')
        return render(request, 'login.html', {
            'next': next,
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid() is not True:
            return render(request, 'login.html', {
                'login_form': login_form,
            })
        else:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next = request.GET.get('next', '')
                print('next')
                print(next)
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {
                    'login_form': login_form,
                    'msg': '用户名或密码错误',
                })


# 用户退出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


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
                'register_form': register_form,
            })
        else:
            username = request.POST.get('email', '')
            if UserProfile.objects.filter(email=username):
                return render(request, 'register.html', {
                    'msg': '用户已存在',
                    'register_form': register_form,
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
            'forget_form': forget_form,
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
        if record:
            if record.is_delete is True:
                print('msg', '验证码已失效')
                return render(request, 'password_reset.html', {
                    'active_code': active_code,
                    'msg': '验证码已失效',
                    'is_expire': True,
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
                'modify_form': modify_form,
            })

        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            return render(request, 'password_reset.html', {
                'email': email,
                'msg': '两次输入的密码不一致',
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


class MyMessageView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        messages = UserMessage.objects.filter()
        current_page = 'message'
        for message in messages:
            message.has_read = True
            message.save()

        # 对讲师数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(messages, per_page=1, request=request)
        messages = p.page(page)

        return render(request, 'usercenter-message.html', {
            'messages': messages,
            'current_page': current_page
        })


class MyFavCourseView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        current_page = 'myfav_course'
        course_list = []
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for fav_course in fav_courses:
            try:
                course = Course.objects.get(id=fav_course.fav_id)
                course_list.append(course)
            except Course.DoesNotExist as e:
                pass
        return render(request, 'usercenter-fav-course.html', {
            'course_list': course_list,
            'current_page': current_page
        })


class MyFavTeacherView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        current_page = 'myfav_teacher'
        teacher_list = []
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
        for fav_teacher in fav_teachers:
            org = Teacher.objects.get(id=fav_teacher.fav_id)
            teacher_list.append(org)
        return render(request, 'usercenter-fav-teacher.html', {
            'teacher_list': teacher_list,
            'current_page': current_page
        })


class MyFavOrgView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        current_page = 'myfavorg'
        org_list = []
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        for fav_org in fav_orgs:
            org = CourseOrg.objects.get(id=fav_org.fav_id)
            org_list.append(org)
        return render(request, 'usercenter-fav-org.html', {
            'org_list': org_list,
            'current_page': current_page
        })


class MyCourseView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        current_page = 'mycourse'
        return render(request, 'usercenter-mycourse.html', {
            'current_page': current_page
        })


class ChangeMobileView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        mobile_form = UpdateMobileForm(request.POST)
        if mobile_form.is_valid():
            mobile = mobile_form.cleaned_data['mobile']
            if UserProfile.objects.filter(mobile=mobile):
                return JsonResponse({
                    'mobile': '该手机号码已经被占用'
                })
            user = request.user
            user.mobile = mobile
            user.username = mobile
            user.save()
            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse(mobile_form.errors)
            # logout(request)


class ChangePwdView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        pwd_form = ChangePwdForm(request.POST)
        if pwd_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            user = request.user
            user.set_password(pwd1)
            user.save()

            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse(pwd_form.errors)


class UploadImageView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse({
                'status': 'fail'
            })


class UserInfoView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        current_page = 'info'
        captcha_form = RegisterGetForm()
        return render(request, 'usercenter-info.html', {
            'captcha_form': captcha_form,
            'current_page': current_page
        })

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse(user_info_form.errors)
