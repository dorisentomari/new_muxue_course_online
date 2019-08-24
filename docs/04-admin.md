# 1. 登录 admin

+ 创建超级用户 `python manage.py createsuperuser`
+ 然后输入用户名，邮箱，密码，创建超级用户成功
+ 访问 `http://127.0.0.1:8000/admin`，就可以登录
+ 在 admin 里显示的各项信息以及如何显示都是由 app 下的 admin.py 文件设定的

# 2. 使用 xadmin 设计 admin

+ 使用 xadmin，原因是界面美观，功能强大
+ 安装，直接使用 pip 安装报错，所以 `pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2`
+ 在 settings.py 中注册应用 `xadmin` 和 `crispy_forms`
+ 然后执行 `makemigrations` 和 `migrate` 命令
