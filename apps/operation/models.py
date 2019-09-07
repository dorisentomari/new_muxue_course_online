# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

from courses.models import Course
from common_model import BaseModel

UserProfile = get_user_model()
FAV_TYPE_CHOICES = ((1, '课程'), (2, '机构'), (3, '讲师'))


# 用户咨询
class UserAsk(BaseModel):
    name = models.CharField(verbose_name=u'姓名', max_length=20)
    mobile = models.CharField(verbose_name=u'手机号', max_length=11)
    course_name = models.CharField(verbose_name=u'课程名', max_length=50)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程评论
class CourseComment(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    comments = models.CharField(verbose_name=u'评论', max_length=200)

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


# 用户收藏
class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name=u'数据id', default=0)
    fav_type = models.IntegerField(verbose_name='类型', choices=FAV_TYPE_CHOICES)

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s 被收藏' % self.fav_type


# 用户信息
class UserMessage(BaseModel):
    user = models.IntegerField(verbose_name=u'用户', default=0)
    message = models.CharField(verbose_name='消息内容', max_length=500)
    has_read = models.BooleanField(verbose_name=u'是否已读', default=False)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '已阅读'


# 用户课程
class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '课程已添加'
