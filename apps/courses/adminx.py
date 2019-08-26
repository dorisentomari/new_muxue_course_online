# -*- encoding: utf-8 -*-

import xadmin

from .models import Course, Lesson, Video, CourseResource


# 在课程页面可以不断添加章节的内容1，嵌套一层，不能多层嵌套
class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    # 列表展示可以显示函数
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'student', 'fav_nums', 'click_nums','create_time', 'update_time', 'is_disable']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'student', 'fav_nums', 'click_nums', 'update_time', 'is_disable']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'student', 'fav_nums', 'click_nums','create_time', 'update_time', 'is_disable']
    # 排序字段设置
    ordering = ['-click_nums']
    # 某些字段我们只能查看，不能修改
    readonly_fields = ['learn_times']
    # 设置某些字段在详情里不显示，不能与只读字段相同，不然不起作用
    exclude = ['click_nums']
    # 在课程页面可以不断添加章节的内容2
    inlines = [LessonInline, CourseResourceInline]
    # 可以直接在列表页面对某些字段进行修改
    list_editable = ['degree', 'desc']
    # 定时刷新
    # refresh_times = [3, 5]


class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'create_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'url', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'create_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'download', 'create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
