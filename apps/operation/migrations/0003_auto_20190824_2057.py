# Generated by Django 2.2.4 on 2019-08-24 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20190824_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomment',
            name='is_delete',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='coursecomment',
            name='is_disable',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否禁用'),
        ),
        migrations.AddField(
            model_name='coursecomment',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='userask',
            name='is_delete',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='userask',
            name='is_disable',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否禁用'),
        ),
        migrations.AddField(
            model_name='userask',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='is_delete',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='is_disable',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否禁用'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='is_delete',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='is_disable',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否禁用'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='is_delete',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='is_disable',
            field=models.BooleanField(auto_created=True, default=False, verbose_name='是否禁用'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
    ]
