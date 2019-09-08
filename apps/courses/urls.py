from django.urls import path

from .views import CourseListView

urlpatterns = [
    path(r'^list/$', CourseListView.as_view(), name="list"),
]
