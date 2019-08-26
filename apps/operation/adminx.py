# -*- encoding: utf-8 -*-

import xadmin

from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'is_disable', 'create_time', 'update_time']
    search_fields = list_display
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['name', 'mobile']
    show_bookmarks = False


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comments', 'is_disable', 'create_time', 'update_time']
    search_fields = list_display
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['comments']
    show_bookmarks = False


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'is_disable', 'create_time', 'update_time']
    search_fields = list_display
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['fav_type']
    show_bookmarks = False


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'is_disable', 'create_time', 'update_time']
    search_fields = list_display
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['message']
    show_bookmarks = False


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'is_disable', 'create_time', 'update_time']
    search_fields = list_display
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    show_bookmarks = False


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
