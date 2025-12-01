from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User, Role
from .models import Category

class CategoryModelsTest(TestCase):
    def test_category_slug_and_str(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(str(category), "Electronics")
        self.assertEqual(category.slug, "electronics")

        category2 = Category.objects.create(name="Electronics ")
        self.assertEqual(category2.slug, "electronics-1")

    def test_category_hierarchy(self):
        parent = Category.objects.create(name="Clothing")
        child = Category.objects.create(name="Men's Clothing", parent=parent)
        self.assertEqual(child.parent, parent)
        self.assertIn(child, parent.children.all())


class CategoryViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.role = Role.objects.create(name="admin")
        self.admin_user = User.objects.create_user(username="adminuser", password="password123", role=self.role, is_staff=True)
        self.normal_user = User.objects.create_user(username="normaluser", password="password123")
        self.category = Category.objects.create(name="Books")

    def test_category_list_view(self):
        response = self.client.get(reverse("category_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Books", [c["name"] for c in response.data])

    def test_category_create_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse("category_list"), {"name": "Toys"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["slug"], "toys")

    def test_category_create_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse("category_list"), {"name": "Toys"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_detail_view(self):
        response = self.client.get(reverse("category_detail", args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Books")

    def test_category_update_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.patch(reverse("category_detail", args=[self.category.id]), {"name": "New Books"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["slug"], "new-books")

    def test_category_update_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.patch(reverse("category_detail", args=[self.category.id]), {"name": "New Books"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_delete_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(reverse("category_detail", args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())

    def test_category_delete_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(reverse("category_detail", args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
