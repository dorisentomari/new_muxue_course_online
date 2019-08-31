# -*- encoding: utf-8 -*-
from django.db import models

from users.models import UserProfile
from courses.models import Course
from apps.common_model import create_time, update_time, is_delete, is_disable


# 用户咨询
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程评论
class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name=u'评论')
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '课程机构'), (3, '讲师名称')), verbose_name='类型')
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s 被收藏' % self.fav_type


# 用户信息
class UserMessage(models.Model):
    user = models.IntegerField(verbose_name=u'用户', default=0)
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(verbose_name=u'是否已读', default=False)
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '已阅读'


# 用户课程
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '课程已添加'
