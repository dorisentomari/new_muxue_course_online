from django.urls import path

from courses.views import CourseListView

urlpatterns = [
    path(r'list/', CourseListView.as_view(), name="list"),
]
