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
    'users',
    'courses',
    'operation',
    'organization'
]
```

# 2. 修改 app 的目录结构

+ 如果我们要创建很多的 app，每一个 app 都放在根目录下，就会有很多文件夹，这样 app 就会与其他的文件混乱。所以为了区分，我们把所有的 app 放入 apps 文件夹下，这样代码目录结构更加清晰明了
+ 根目录下创建 apps 文件夹，然后把 users、courses、operation、organization 文件夹全部剪切到 apps 文件夹下
+ 但是 Django 默认是在根目录下寻找每一个 app 的，我们把 app 移走了，那么 Django 就找不到了， 所以我们要告诉 Django 去哪里找 app
+ 修改 settings.py，在 BASE_DIR 下边添加代码，这样就 Django 就可以识别到 app

```python
import sys

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```

# 3. 关于 Django 自带的 model

+ Django 默认带了很多的数据表，同时也有创建数据表的命令
+ 首先我们看两个命令，makemigrations 和 migrate
+ `python manage.py makemigrations`
+ `python manage.py migrate`
+ makemigrations 的命令是在 app 下的 migrations 文件夹里记录该 app 下的 models.py 变动的记录，注意此时还没有修改数据库自身，仅仅是创建了记录
+ migrate 是把 app 下的 migrations 修改记录作用到数据库，调用这个命令才正式修改数据库
+ 如果此时没有任何的 app，那么这两条命令的操作是调用 Django 默认的数据库的设定
+ 所以默认情况下使用这两条命令，我们可以在数据库中看到默认创建的数据表的名字

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| test_django        |
+--------------------+

mysql> show tables;
+----------------------------+
| Tables_in_test_django      |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
```

+ 默认数据表的说明
    + auth_group 权限组表
    + auth_permission 权限表
    + auth_group_permissions 权限组表和权限表的对应关系表
    + auth_user 用户表
    + auth_user_groups 用户组表
    + auth_user_user_permissions 用户表与权限表的对应关系表
    + django_admin_log 管理日志表
    + django_content_type 记录 app_label ，每个 app_label 下的 modle 显示名称，和 model 模块名。用来显示 admin 首页     
    + django_migrations 数据表迁移记录
    + django_session 存储 session 表

# 3. [关于app的一些介绍](http://www.conyli.cc/chapter01.html)

+ `admin.py`，用户将模型注册到管理后台，以便在 Django 的管理后台查看，管理后台是一个可选的应用
+ `apps.py`，当前应用的主要配置文件
+ `migrations.py`，包含应用的数据迁移记录，用来追踪数据模型的变化然后与数据库进行同步
+ `models.py`，当前应用的数据模型，所有的应用都必须有一个`models.py`，但是其中的内容可以为空
+ `test.py`，添加测试代码的文件
+ `views.py`，应用的业务逻辑部分，每一个视图接收一个 HTTP 请求，然后返回一个 HTTP 响应
+ 每一个应用都必须在 settings.py 的`INSTANLLED_APPS`中激活
