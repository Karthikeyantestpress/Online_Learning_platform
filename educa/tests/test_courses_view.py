from .test_model_mixin_testcases import ModelMixin
from django.test import TestCase
from django.urls import reverse
from courses.models import Course


class TestCoursesListView(ModelMixin, TestCase):
    def test_list_view_displays_the_courses_for_the_permitted_user(self):

        self.client.login(username="testuser", password="123")
        response = self.client.get(reverse("course:manage_course_list"))
        self.assertQuerysetEqual(
            response.context.get("object_list"), [self.courses]
        )

    def test_list_view_returns_403_for_the_non_permitted_user(self):

        self.client.login(username="test", password="123")
        response = self.client.get(reverse("course:manage_course_list"))
        self.assertEqual(response.status_code, 403)


class TestCoursesCreateView(ModelMixin, TestCase):
    def test_create_view_creates_new_course_for_the_user(self):

        self.client.login(username="testuser", password="123")
        self.client.post(
            reverse("course:create"),
            data={
                "subject": self.subject,
                "title": "test course_1",
                "slug": "test-course-1",
                "overview": "sample course",
            },
        )
        response = self.client.get(reverse("course:manage_course_list"))
        new_course_created = Course.objects.get(id=1)
        self.assertQuerysetEqual(
            response.context.get("object_list"), [new_course_created]
        )
