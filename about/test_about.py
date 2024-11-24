from django.test import TestCase
from .models import About

class AboutModelTest(TestCase):
    def test_about_model_str_method(self):
        about = About.objects.create(title='About Us', content='This is an about page')
        self.assertEqual(str(about), about.title)




