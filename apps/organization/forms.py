# -*- encoding: utf-8 -*-
import re

from django import forms

from operation.models import UserAsk

from config.constant import regex_mobile


class AddAskForm(forms.Form):
    mobile = forms.CharField(max_length=11, min_length=11, required=True, error_messages={
        'required': '手机号不能为空',
        'min_length': '手机号必须为 11 位',
        'max_length': '手机号必须为 11 位',
    })
    name = forms.CharField(required=True, error_messages={
        'required': '姓名不能为空',
    })
    course_name = forms.CharField(required=True, error_messages={
        'required': '课程名不能为空',
    })


class AddAskModelForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")
