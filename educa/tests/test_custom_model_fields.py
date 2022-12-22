from .test_model_mixin_testcases import ModelMixin
from django.test import TestCase


class TestModel(ModelMixin, TestCase):
    def test_order_field_generates_automatically(self):
        modules = self.create_new_modules(count=5)
        self.assertEqual(modules.first().order, 0)
        self.assertEqual(modules.last().order, 4)

    def test_order_field_accepts_custom_order_number(self):
        modules = self.create_new_modules(count=1, order_number=100)
        self.assertEqual(modules.first().order, 100)
