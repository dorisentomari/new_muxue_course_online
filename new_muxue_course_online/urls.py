from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from django.conf.urls.static import static

import xadmin

from users.views import LoginView, LogoutView, RegisterView, ActiveUserView, \
    ForgetPasswordView, ResetView, ModifyView

from new_muxue_course_online.settings import MEDIA_ROOT

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('xadmin/', xadmin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('active/<active_code>', ActiveUserView.as_view(), name='user_active'),
    path('forget_pwd/', ForgetPasswordView.as_view(), name='forget_pwd'),
    path('reset/<active_code>', ResetView.as_view(), name='reset_password'),
    path('modify_pwd/', ModifyView.as_view(), name='modify_password'),

    path('org/', include(('apps.organization.urls', 'organization'), namespace="org")),
    path('courses/', include(('apps.courses.urls', 'courses'), namespace="course")),
]

urlpatterns += static('/media/', document_root=MEDIA_ROOT)
