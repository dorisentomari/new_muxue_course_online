# -*- encoding: utf-8 -*-
from django.db import models

from apps.common_model import create_time, update_time, is_delete, is_disable

category_choices = (('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校'))


class CityDict(models.Model):
    name = models.CharField(verbose_name=u'城市', max_length=20)
    desc = models.CharField(verbose_name=u'描述', max_length=200)
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(verbose_name=u'机构名称', max_length=50)
    category = models.CharField(verbose_name='机构类别', max_length=20, choices=category_choices, default='pxjg')
    desc = models.CharField(verbose_name=u'机构描述', max_length=100)
    click_num = models.IntegerField(verbose_name=u'点击数量', default=0)
    fav_num = models.IntegerField(verbose_name=u'收藏数量', default=0)
    image = models.ImageField(verbose_name=u'封面图', upload_to='org/%Y/%m')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市', on_delete=models.CASCADE)
    address = models.CharField(verbose_name=u'机构地址', max_length=150)
    students = models.IntegerField(verbose_name=u'学习人数', default=0)
    course_nums = models.IntegerField(verbose_name=u'课程数量', default=0)
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(verbose_name=u'教师名字', max_length=10)
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='年龄', default=18)
    work_years = models.IntegerField(verbose_name=u'工作年限', default=0)
    work_company = models.CharField(verbose_name=u'就职公司', max_length=50)
    work_position = models.CharField(verbose_name=u'公司职位', max_length=50)
    avatar = models.ImageField(verbose_name=u'头像', max_length=200, upload_to='teacher/%Y/%m', null=True, blank=True)
    points = models.CharField(verbose_name=u'教学特点', max_length=50)
    click_num = models.IntegerField(verbose_name=u'点击数量', default=0)
    fav_num = models.IntegerField(verbose_name=u'收藏数量', default=0)
    create_time = create_time
    update_time = update_time
    is_disable = is_disable
    is_delete = is_delete

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
