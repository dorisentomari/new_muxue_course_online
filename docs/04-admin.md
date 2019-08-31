# 1. 登录 admin

+ 创建超级用户 `python manage.py createsuperuser`
+ 然后输入用户名，邮箱，密码，创建超级用户成功
+ 访问 `http://127.0.0.1:8000/admin`，就可以登录
+ 在 admin 里显示的各项信息以及如何显示都是由 app 下的 admin.py 文件设定的

# 2. 使用 xadmin 设计 admin

+ 使用 xadmin，原因是界面美观，功能强大。Django 自带的 admin 管理系统不够好用
+ 安装，直接使用 pip 安装报错，所以 `pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2`
+ 在 settings.py 中注册应用 `xadmin` 和 `crispy_forms`
+ 然后执行 `makemigrations` 和 `migrate` 命令，xadmin 会创建三张关于 xadmin 的数据表
+ 在每一个 app 下新建一个 adminx.py 文件，xadmin 会自动读取每一个 app 下的 adminx.py 文件
+ adminx.py 文件的配置与 admin.py 配置基本一样，只是 adminx.py 自己添加了一些新的特性和样式操作
+ ps: 如果要是使用 xadmin 的时候感觉页面或者功能需要修改，可以直接把 env 里的 xadmin 剪切到 extra_apps 里，这样我们就可以对 xadmin 做自己的修改。但是需要在 settings.py 里添加 `sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))`

# 3. 修改 adminx.py

+ xadmin 注册每一个 model 的时候，必须是在 models 里的类名后边添加 `Admin`，比如 models 里的 EmailVerifyRecord，在这里需要改为 EmailVerifyRecordAdmin
+ adminx.py 里类的属性
    + list_display 展示列表需要显示的字段信息
    + search_fields 搜索框里可以搜索的字段信息
    + list_filter 可以索索过滤的字段信息
+ 每一个 model 都需要进行注册

```python
from .models import Course, Lesson, Video, CourseResource


# 在课程页面可以不断添加章节的内容，嵌套一层，不能多层嵌套
class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    # 列表展示可以显示函数
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'student', 'fav_nums', 'click_nums', 'is_disable', 'create_time', 'update_time']
    # 搜索的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'student', 'fav_nums', 'click_nums', 'is_disable']
    # 过滤的字段
    list_filter = list_display
    # 查看详情的字段
    show_detail_fields = ['name']
    # 排序字段设置
    ordering = ['-click_nums', 'create_time']
    # 某些字段我们只能查看，不能修改
    readonly_fields = ['learn_times', 'create_time', 'update_time']
    # 设置某些字段在详情里不显示，不能与只读字段相同，不然不起作用
    exclude = ['click_nums']
    # 在课程页面可以不断添加章节的内容
    inlines = [LessonInline, CourseResourceInline]
    # 可以直接在列表页面对某些字段进行修改
    list_editable = ['desc', 'detail', 'degree', 'is_disable']
    # 定时刷新
    # refresh_times = [3, 5]
    # 是否显示书签
    show_bookmarks = False
    # 书签列表配置
    list_bookmarks = [{}]
    # 指定菜单的 icon
    model_icon = 'fa fa-circle-o'
    
    
xadmin.site.register(Course, CourseAdmin)
```

# 4. xadmin 全局属性

+ 全局属性的配置是固定的写法

```python
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


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
```
