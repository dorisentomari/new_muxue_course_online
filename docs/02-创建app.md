# 1. 创建 app

app 实际上就是每一个单独的功能模块，但是不是说每一个 app 之间没有任何关系，app 之间是可以调用功能的，但是为了模块拆分，可以把不同的功能模块做成对应的 app

+ 创建 app，`django-admin startapp <appName>`
+ 我们一共需要 4 个服务，所以创建 4 个 app
+ `django-admin startapp users`
+ `django-admin startapp courses`
+ `django-admin startapp organization`
+ `django-admin startapp operation`
+ 每一个 app 都需要注册到 settings.py 的 INSTALLED_APPS 中，这样 Django 才能够使用这个 app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

# 2. [关于settings.py的一些配置](http://www.conyli.cc/chapter01.html)
+ `BASE_DIR`为该项目的根目录
+ `DEBUG`是一个布尔值，控制 DEBUG 模式的开启或关闭，当设置为`True`时，Django 将会把所有的日志和错误信息都输出到控制台，生产环境必须设置为`False`，否则会导致信息泄露
+ `ALLOWED_HOSTS`在本地开发的时候，无需设置。在生产环境中，`DEBUG`设置为`FASLE`，必须将主机名/IP地址填入该列表，让 Django 为该主机/IP提供服务
+ `INSTALLED_APPS`列出了每一个项目当前激活的应用，默认包含以下应用
    + `django.contrib.admin`，管理后台应用
    + `django.contrib.auth`，用户身份认证
    + `django.contrib.contenttypes`，追踪 ORM 模型与应用的对应关系
    + `django.contrib.sessions`，session 应用
    + `django.contrib.messages`，消息应用
    + `django.contrib.staticfiles`，管理站点静态资源
+ `MIDDLEWARE`是中间件列表
+ `ROOT_URLCONF`指定项目的根 URL patterns 配置文件
+ `DATABASE`是一个字典，包含不同名称的数据库及其具体位置，必须始终有一个默认的`default`数据库，默认使用 `SQLlit3` 数据库
+ `LANGUAGE_CODE`站点默认的语言代码
+ `USE_TZ`是否启用时区支持，Django 可以根据时区自动切换时间显示。

# 4. [关于app的一些介绍](http://www.conyli.cc/chapter01.html)
+ `admin.py`，用户将模型注册到管理后台，以便在 Django 的管理后台查看，管理后台是一个可选的应用
+ `apps.py`，当前应用的主要配置文件
+ `migrations.py`，包含应用的数据迁移记录，用来追踪数据模型的变化然后与数据库进行同步
+ `models.py`，当前应用的数据模型，所有的应用都必须有一个`models.py`，但是其中的内容可以为空
+ `test.py`，添加测试代码的文件
+ `views.py`，应用的业务逻辑部分，每一个视图接收一个 HTTP 请求，然后返回一个 HTTP 响应
+ 每一个应用都必须在 settings.py 的`INSTANLLED_APPS`中激活
