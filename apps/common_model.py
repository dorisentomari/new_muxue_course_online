# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models

create_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
is_disable = models.BooleanField(verbose_name=u'是否禁用', default=False)
is_delete = models.BooleanField(verbose_name=u'是否删除', default=False)
