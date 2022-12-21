from django.views.generic.list import ListView
from .models import Course
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


class OwnerMixin(object):
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)


class OwnerCourseMixin(
    OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin
):
    model = Course
    fields = ["subject", "title", "slug", "overview"]
    success_url = reverse_lazy("course:manage_course_list")


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = "courses/manage/course/list.html"
    permission_required = "courses.view_course"
