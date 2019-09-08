from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q

from pure_pagination import Paginator, PageNotAnInteger

from apps.courses.models import Course


class CourseListView(View):
    pass
