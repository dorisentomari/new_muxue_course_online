# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher
from apps.common_model import add_time, update_time, is_delete, is_disable


# 每一个课程
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名字', blank=False)
    desc = models.CharField(max_length=300, verbose_name='课程描述', blank=True, default='')
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构', null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='授课讲师', null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, verbose_name='课程类别', blank=False)
    tag = models.CharField(max_length=10, verbose_name='课程标签', default='')
    detail = models.TextField(max_length=1024, verbose_name='课程详情', default='')
    degree = models.CharField(max_length=2, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), verbose_name='难度')
    learn_times = models.IntegerField(verbose_name='学习次数', default=0)
    student = models.IntegerField(verbose_name='学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    image = models.ImageField(max_length=200, verbose_name='封面图', upload_to='courses/%Y/%m')
    click_nums = models.IntegerField(verbose_name='点击次数', default=0)
    need_know = models.CharField(max_length=300, verbose_name='课程须知', default='')
    tell_you = models.CharField(max_length=300, verbose_name='你能学到什么', default='')
    add_time = add_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 每一个章节
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'章节名称', blank=False)
    add_time = add_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 每一个视频资源
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    url = models.CharField(max_length=200, verbose_name=u'访问地址')
    learn_times = models.IntegerField(verbose_name='学习次数', default=0)
    add_time = add_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 每一个课程资源
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(max_length=100, verbose_name='资源文件', upload_to='course/resource/%Y/%m')
    add_time = add_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 轮播图
class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True
