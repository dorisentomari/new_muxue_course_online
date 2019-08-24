# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    category = models.CharField(max_length=20, default='pxjg', choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')),
                                verbose_name='机构类别')
    desc = models.CharField(verbose_name=u'机构描述', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name=u'点击数量')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数量')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u'封面图')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市', on_delete=models.CASCADE)
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    course_nums = models.IntegerField(default=0, verbose_name='课程数量')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'教师名字')
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='年龄', default=18)
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    avatar = models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像', max_length=200, null=True, blank=True)
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数量')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数量')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
