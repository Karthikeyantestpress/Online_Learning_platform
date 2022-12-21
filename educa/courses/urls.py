from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path(
        "mine/",
        views.ManageCourseListView.as_view(),
        name="manage_course_list",
    ),
]
