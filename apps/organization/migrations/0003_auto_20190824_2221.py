# Generated by Django 2.2.4 on 2019-08-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20190824_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydict',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='citydict',
            name='is_disable',
            field=models.BooleanField(default=False, verbose_name='是否禁用'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='is_disable',
            field=models.BooleanField(default=False, verbose_name='是否禁用'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='is_disable',
            field=models.BooleanField(default=False, verbose_name='是否禁用'),
        ),
    ]
