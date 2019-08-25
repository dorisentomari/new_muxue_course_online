# -*- encoding: utf-8 -*-

import xadmin

from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin(object):
    list_display = ['desc', 'name', 'add_time', 'update_time', 'is_disable']
    search_fields = ['desc', 'name']
    list_filter = ['desc', 'name', 'add_time', 'update_time', 'is_disable']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'address', 'city', 'add_time', 'update_time', 'is_disable']
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'address', 'city']
    list_filter = ['name', 'desc', 'click_num', 'fav_num', 'address', 'city', 'add_time', 'update_time', 'is_disable']
    # 这个外键可以采用ajax方法获取字段
    relfield_style = 'fk_ajax'


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company',
                    'work_position', 'points', 'click_num', 'fav_num', 'add_time', 'update_time', 'is_disable']
    search_fields = ['name', 'org', 'work_years', 'work_company',
                     'work_position', 'points', 'click_num', 'fav_num']
    list_filter = ['name', 'org', 'work_years', 'work_company',
                   'work_position', 'points', 'click_num', 'fav_num', 'add_time', 'update_time', 'is_disable']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
