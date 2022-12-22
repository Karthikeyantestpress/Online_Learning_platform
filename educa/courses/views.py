from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Course
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class OwnerMixin(object):
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(
            self.request, "New course has been added successfully"
        )
        return super().form_valid(form)


class OwnerCourseMixin(
    OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin
):
    model = Course
    fields = ["subject", "title", "slug", "overview"]
    success_url = reverse_lazy("course:manage_course_list")


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = "courses/manage/course/form.html"


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = "courses/manage/course/list.html"
    permission_required = "courses.view_course"


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = "courses.add_course"
