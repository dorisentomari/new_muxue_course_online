# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models

add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')
is_disable = models.BooleanField(verbose_name=u'是否禁用', default=False, auto_created=True)
is_delete = models.BooleanField(verbose_name=u'是否删除', default=False, auto_created=True)
