from django.urls import path

from organization.views import OrgView

urlpatterns = [
    path(r'list/', OrgView.as_view(), name="list"),
]

