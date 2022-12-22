from django.test import TestCase
from courses.models import Subject, Course, Module
from .factories import UserFactory
from django.contrib.auth.models import User


class ModelMixin(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="test",
            password="123",
        )

        self.crededntial = {"username": "testuser", "password": "123"}
        self.user = UserFactory(**self.crededntial)

        self.subject = Subject.objects.create(
            title="testsubject",
            slug="testsubject",
        )
        self.courses = Course.objects.create(
            owner=self.user,
            subject=self.subject,
            title="testcourse",
            slug="testcourse",
        )

    def create_new_modules(self, count, order_number=None):
        for _ in range(count):
            Module.objects.create(
                course=self.courses,
                title="testmodule",
                order=order_number,
            )
        return Module.objects.all()
