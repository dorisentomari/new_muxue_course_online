# 1. 创建 models

+ 每一个 app 下都有一个对应的 models.py，这个 models 是与该 app 直接相关的数据表模型
+ 在这个 models 里可以有多个数据表，每一个数据表都是一个类，但是这个类必须继承 Django 下 db 的 models.Model 类
+ `from django.db import models`
+ 在每一个 model 里，可以定义数据表需要用到的字段名，字段类型，比如说字符串字段 CharField，字段的属性
+ 类的元属性，包括数据库的名字，索引，排序，复数，联合主键等

```python
from datetime import datetime

from django.db import models


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱地址')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=10,
                                 verbose_name='验证码类型')
    send_time = models.TimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        # 数据表的名字
        verbose_name = u'邮箱验证码'
        # 数据表的复数名字，如果不设定，那么 Django 会自动给数据表名后边加 s
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
```

# 2. 关于 users 数据表

+ Django 会默认帮我们创建一个 users 数据表，叫 auth_user，里边定义了很多字段及属性，我们默认创建的用户信息，就保存在这个数据表里
+ 但是，这个数据表里的字段不一定满足我们的业务需求，所以我们需要修改/重写 users 这个数据表
+ 有一个但是，我们虽然修改/重写 users 这个数据表，但是我们还想用 Django 已经对这个数据表做好的一些操作，比如 session 等
+ 所以，我们创建的 users 表需要继承 Django 默认的 users 表
+ `from django.contrib.auth.models import AbstractUser`
+ 这里如果我们自己写的字段与默认的字段重复，那么就会重写该字段，如果没有重复，那么就创建该字段
+ 当我们自己重写了 users，我们还要在 settings 里告诉 Django 我们要使用那个 users 表
+ `AUTH_USER_MODEL = 'users.UserProfile'`

```python
from django.db import models
# AbstractUser是数据库中auth_user数据表里的字段
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', default=u'')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=((u'male', u'男'), (u'female', u'女')), default=u'', max_length=10)
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
```

# 3. models 之间的关系

+ org 下是 course，teacher，city
+ course 下是 lesson
+ lesson 下是 video
+ user 相关的是 operation 下的 userAsk，userComment，userCourse，userFavorite，userMessage
