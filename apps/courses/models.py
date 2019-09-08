# -*- encoding: utf-8 -*-

from django.db import models

from organization.models import CourseOrg, Teacher
from common_model import BaseModel


# 每一个课程
class Course(BaseModel):
    name = models.CharField(verbose_name=u'课程名字', max_length=50, blank=False)
    desc = models.CharField(verbose_name=u'课程描述', max_length=300, blank=True, default='')
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'课程机构', null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name=u'授课讲师', null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(verbose_name=u'课程类别', max_length=50, blank=False)
    tag = models.CharField(verbose_name=u'课程标签', max_length=10, default='')
    detail = models.TextField(verbose_name=u'课程详情', max_length=1024, default='')
    degree = models.CharField(verbose_name=u'难度', max_length=2, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')))
    learn_times = models.IntegerField(verbose_name=u'学习次数', default=0)
    student = models.IntegerField(verbose_name=u'学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name=u'收藏人数', default=0)
    image = models.ImageField(verbose_name=u'封面图', max_length=200, upload_to='courses/%Y/%m')
    click_nums = models.IntegerField(verbose_name=u'点击次数', default=0)
    need_know = models.CharField(verbose_name=u'课程须知', max_length=300, default='')
    tell_you = models.CharField(verbose_name=u'你能学到什么', max_length=300, default='')
    is_classics = models.BooleanField(default=False, verbose_name="是否经典")

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 每一个章节
class Lesson(BaseModel):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'章节名称', max_length=100, blank=False)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 每一个视频资源
class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'视频名称', max_length=100)
    url = models.CharField(verbose_name=u'访问地址', max_length=200)
    learn_times = models.IntegerField(verbose_name='学习次数', default=0)

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 每一个课程资源
class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'名称', max_length=100)
    file = models.FileField(verbose_name=u'资源文件', max_length=100, upload_to='course/resource/%Y/%m')

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
