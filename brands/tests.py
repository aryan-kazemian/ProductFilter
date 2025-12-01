from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status

from accounts.models import User, Role
from accounts.permissions import IsAdmin
from brands.models import Brand
from brands.serializers import BrandSerializer


class BrandModelsTest(TestCase):
    def test_brand_slug_and_str(self):
        brand = Brand.objects.create(name="Nike")
        self.assertEqual(str(brand), "Nike")
        self.assertEqual(brand.slug, "nike")

        duplicate = Brand.objects.create(name="Nike ")
        self.assertEqual(duplicate.slug, "nike-1")

class BrandSerializersTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Adidas")

    def test_brand_serializer_fields(self):
        serializer = BrandSerializer(self.brand)
        data = serializer.data
        self.assertEqual(data["name"], "Adidas")
        self.assertEqual(data["slug"], "adidas")


class BrandViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

        self.role = Role.objects.create(name="Manager")
        self.admin_user = User.objects.create_user(username="admin", password="pass", is_staff=True, role=self.role)
        self.normal_user = User.objects.create_user(username="user", password="pass", is_staff=False, role=self.role)

        self.brand = Brand.objects.create(name="Puma")

        self.list_url = reverse("brand_list")
        self.detail_url = reverse("brand_detail", args=[self.brand.pk])

    def test_brand_list_view_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Puma", [b["name"] for b in response.data])

    def test_brand_create_view_admin_only(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(self.list_url, {"name": "Reebok"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.list_url, {"name": "Reebok"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["slug"], "reebok")

    def test_brand_detail_update_permission(self):
        data = {"name": "Puma Updated"}

        self.client.force_authenticate(user=self.normal_user)
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Puma Updated")

    def test_brand_detail_delete_permission(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class IsAdminPermissionTest(TestCase):

    def setUp(self):
        self.permission = IsAdmin()
        self.factory = APIRequestFactory()
        self.role = Role.objects.create(name="RoleX")

        self.staff_user = User.objects.create_user(username="staff", password="pass", is_staff=True, role=self.role)
        self.normal_user = User.objects.create_user(username="normal", password="pass", is_staff=False, role=self.role)

    def test_permission_granted_for_staff_user(self):
        request = self.factory.get("/dummy/")
        request.user = self.staff_user
        self.assertTrue(self.permission.has_permission(request, None))

    def test_permission_denied_for_normal_user(self):
        request = self.factory.get("/dummy/")
        request.user = self.normal_user
        self.assertFalse(self.permission.has_permission(request, None))
