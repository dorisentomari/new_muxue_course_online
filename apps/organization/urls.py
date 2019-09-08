from django.urls import path

from organization.views import OrgView, AddAskView

urlpatterns = [
    path(r'list/', OrgView.as_view(), name="list"),
    path(r'add_ask/', AddAskView.as_view(), name="add_ask"),
]

