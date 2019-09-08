# -*- encoding: utf-8 -*-
import os

from datetime import datetime

from django.db import models
# AbstractUser是数据库中auth_user数据表里的字段
from django.contrib.auth.models import AbstractUser

from apps.common_model import BaseModel

GENDER_CHOICES = ((u'male', u'男'), (u'female', u'女'))
SEND_TYPE_CHOICES = ((u'register', u'注册'), (u'forget', u'找回密码'))


def get_image_path(instance, filename):
    return os.path.join('image', filename)


class UserProfile(AbstractUser, BaseModel):
    nickname = models.CharField(verbose_name=u'昵称', max_length=50, default=u'')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(verbose_name=u'性别', max_length=6, choices=GENDER_CHOICES, default=u'')
    address = models.CharField(verbose_name=u'地址', max_length=100, null=True, default=u'')
    mobile = models.CharField(verbose_name=u'手机号', max_length=11, null=True, blank=True)
    image = models.ImageField(verbose_name=u'头像', max_length=100, upload_to=get_image_path,
                              default=u'image/default.jpg')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    # def unread_nums(self):
    #     # 未读消息数量
    #     return self.usermessage_set.filter(has_read=False).count()


class EmailVerifyRecord(BaseModel):
    code = models.CharField(verbose_name=u'验证码', max_length=20)
    email = models.EmailField(verbose_name=u'邮箱地址', max_length=50)
    send_type = models.CharField(verbose_name=u'验证码类型', max_length=10, choices=SEND_TYPE_CHOICES)
    send_time = models.TimeField(verbose_name=u'发送时间', default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(BaseModel):
    title = models.CharField(max_length=100, verbose_name=u'轮播图标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'轮播图顺序')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
