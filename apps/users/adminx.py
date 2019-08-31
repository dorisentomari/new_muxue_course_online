# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row

from .models import EmailVerifyRecord, Banner, UserProfile


class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('', 'username', 'password', css_class='unsort no_title'),
                    Fieldset(_('Personal info'), Row('nickname', 'birthday', 'mobile', 'gender', 'address'), 'email'),
                    Fieldset(_('Permissions'), 'groups', 'user_permissions'),
                    Fieldset(_('Important dates'), 'last_login', 'date_joined'),
                ),
                Side(
                    Fieldset(_('Status'), 'is_disable', 'is_staff', 'is_superuser', ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


class EmailVerifyRecordAdmin(object):
    # 以列表形式展示内容
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 可以在搜索框进行搜索的字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤搜索的字段，在页面上显示的是值
    list_filter = list_display


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time', 'update_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = list_display
    readonly_fields = ['create_time', 'update_time']
    list_editable = ['title', 'image', 'url', 'index']
    show_bookmarks = False


# 修改全局主题样式
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 修改全局文字内容
class GlobalSettings(object):
    site_title = 'NEW MUXUE LEARN'
    site_footer = 'NEW MUXUE COMPANY ONLINE SITE'
    # 菜单样式可以折叠
    menu_style = 'accordion'


class IndexViewSettings(object):
    title = '工作台'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.IndexView, IndexViewSettings)
