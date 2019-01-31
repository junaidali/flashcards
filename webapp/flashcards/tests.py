from django.test import TestCase
from django.urls import reverse
from .models import Category

# Create your tests here.
class CategoryModelTests(TestCase):
    def test_no_categories(self):
        """
        If no categories are defined, than homepage shows default message
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
    
    def test_one_category(self):
        """
        If one category exists, it shoudl be displayed on homepage
        """
        category1 = Category(name_primary="DemoCategory", name_secondary="عرض")
        category1.save()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DemoCategory')
        self.assertContains(response, 'عرض')
