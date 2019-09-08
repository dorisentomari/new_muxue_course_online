import re

from django import forms
from operation.models import UserFavorite, CourseComment


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CourseComment
        fields = ["course", "comments"]
