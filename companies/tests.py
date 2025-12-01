from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User, Role
from .models import Company

class CompanyModelsTest(TestCase):
    def test_company_slug_and_str(self):
        comp = Company.objects.create(name="TechCorp")
        self.assertEqual(str(comp), "TechCorp")
        self.assertEqual(comp.slug, "techcorp")

        comp2 = Company.objects.create(name="TechCorp ")
        self.assertEqual(comp2.slug, "techcorp-1")


class CompanyViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.role = Role.objects.create(name="admin")
        self.admin_user = User.objects.create_user(username="adminuser", password="password123", role=self.role, is_staff=True)
        self.normal_user = User.objects.create_user(username="normaluser", password="password123")
        self.comp = Company.objects.create(name="InnovateLtd")

    def test_company_list_view(self):
        response = self.client.get(reverse("company_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("InnovateLtd", [c["name"] for c in response.data])

    def test_company_create_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse("company_list"), {"name": "FutureTech"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["slug"], "futuretech")

    def test_company_create_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse("company_list"), {"name": "FutureTech"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_company_detail_view(self):
        response = self.client.get(reverse("company_detail", args=[self.comp.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "InnovateLtd")

    def test_company_update_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.patch(reverse("company_detail", args=[self.comp.id]), {"name": "InnovateLtdNew"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["slug"], "innovateltdnew")

    def test_company_update_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.patch(reverse("company_detail", args=[self.comp.id]), {"name": "InnovateLtdNew"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_company_delete_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(reverse("company_detail", args=[self.comp.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Company.objects.filter(id=self.comp.id).exists())

    def test_company_delete_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(reverse("company_detail", args=[self.comp.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
