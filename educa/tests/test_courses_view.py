from .test_model_mixin_testcases import ModelMixin
from django.test import TestCase
from django.urls import reverse


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
