# -*- encoding: utf-8 -*-
from random import Random
from django.core.mail import send_mail
from new_muxue_course_online.settings import EMAIL_FROM

from users.models import EmailVerifyRecord


def generate_random_str(random_length=8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = generate_random_str(18)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = '慕雪在线网注册激活链接'
        email_body = '请点击链接激活您的账号:http://127.0.0.1:8000/active/{0}'.format(code)
        try:
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                return True
        except:
            return False

    elif send_type == 'forget':
        email_title = '慕雪在线网密码重置'
        email_body = '请点击下边的链接重置您的账号:http://127.0.0.1:8000/reset/{0}'.format(code)
        try:
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                return True
        except:
            return False
