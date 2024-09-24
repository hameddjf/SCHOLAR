from django.test import TestCase
from django.urls import reverse

from .models import Category, Tag


class CategoryModelTest(TestCase):
    """Test cases for Category model"""

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", slug="test-category")

    def test_category_creation(self):
        """Test category creation"""
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.slug, "test-category")

    def test_category_str(self):
        """Test category string representation"""
        self.assertEqual(str(self.category), "Test Category")


class TagModelTest(TestCase):
    """Test cases for Tag model"""

    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag", slug="test-tag")

    def test_tag_creation(self):
        """Test tag creation"""
        self.assertEqual(self.tag.name, "Test Tag")
        self.assertEqual(self.tag.slug, "test-tag")

    def test_tag_str(self):
        """Test tag string representation"""
        self.assertEqual(str(self.tag), "Test Tag")


class CategoryViewsTest(TestCase):
    """Test cases for Category views"""

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", slug="test-category")

    def test_category_list_view(self):
        """Test category list view"""
        response = self.client.get(reverse('tags:category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")

    def test_category_detail_view(self):
        """Test category detail view"""
        response = self.client.get(
            reverse('tags:category_detail', kwargs={'slug': 'test-category'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Category: Test Category")


class TagViewsTest(TestCase):
    """Test cases for Tag views"""

    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag", slug="test-tag")

    def test_tag_list_view(self):
        """Test tag list view"""
        response = self.client.get(reverse('tags:tag_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tag")

    def test_tag_detail_view(self):
        """Test tag detail view"""
        response = self.client.get(
            reverse('tags:tag_detail', kwargs={'slug': 'test-tag'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tag: Test Tag")
