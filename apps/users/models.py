# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models
# AbstractUser是数据库中auth_user数据表里的字段
from django.contrib.auth.models import AbstractUser

from apps.common_model import create_time, update_time, is_delete, is_disable

# Create your models here.

gender_choices = ((u'male', u'男'), (u'female', u'女'))
send_type_choices = (('register', u'注册'), ('forget', u'找回密码'))


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', default=u'')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default=u'')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default=u'image/default.png')
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱地址')
    send_type = models.CharField(max_length=10, verbose_name='验证码类型', choices=send_type_choices)
    send_time = models.TimeField(default=datetime.now, verbose_name='发送时间')
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'轮播图标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'轮播图顺序')
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
