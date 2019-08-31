# -*- encoding: utf-8 -*-

import xadmin

from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin(object):
    list_display = ['desc', 'name', 'is_disable', 'create_time', 'update_time']
    search_fields = ['desc', 'name']
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['desc', 'name', 'is_disable']
    show_bookmarks = False


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'address', 'city', 'is_disable', 'create_time',
                    'update_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_num', 'address', 'city']
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    # 这个外键可以采用ajax方法获取字段
    relfield_style = 'fk_ajax'
    list_editable = ['name', 'desc', 'address', 'city']
    show_bookmarks = False


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company',
                    'work_position', 'points', 'click_num', 'fav_num', 'is_disable', 'create_time', 'update_time']
    search_fields = ['name', 'org', 'work_years', 'work_company',
                     'work_position', 'points', 'click_num', 'fav_num']
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['name', 'org', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_num',
                     'is_disable']
    show_bookmarks = False


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
