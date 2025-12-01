from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status

from accounts.models import User, Role
from accounts.permissions import IsAdmin
from attributes.models import Country, Color, Gender, Age, Season, Tag
from attributes.serializers import (
    CountrySerializer, ColorSerializer, GenderSerializer,
    AgeSerializer, SeasonSerializer, TagSerializer
)


class AttributesModelsTest(TestCase):
    def test_country_slug_and_str(self):
        country = Country.objects.create(name="United States")
        self.assertEqual(str(country), "United States")
        self.assertEqual(country.slug, "united-states")

    def test_color_slug_and_str(self):
        color = Color.objects.create(name="Red", color="#FF0000")
        self.assertEqual(str(color), "Red")
        self.assertEqual(color.slug, "red")

    def test_gender_slug_and_str(self):
        gender = Gender.objects.create(name="male")
        self.assertEqual(str(gender), "male")
        self.assertEqual(gender.slug, "male")

    def test_age_slug_and_str(self):
        age = Age.objects.create(name="Teen", min_age=13, max_age=19)
        self.assertEqual(str(age), "Teen")
        self.assertEqual(age.slug, "teen")

    def test_season_slug_and_str(self):
        season = Season.objects.create(name="Summer")
        self.assertEqual(str(season), "Summer")
        self.assertEqual(season.slug, "summer")

    def test_tag_slug_and_str(self):
        tag = Tag.objects.create(name="NewArrival")
        self.assertEqual(str(tag), "NewArrival")
        self.assertEqual(tag.slug, "newarrival")


class AttributesSerializersTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Canada")
        self.color = Color.objects.create(name="Blue", color="#0000FF")
        self.gender = Gender.objects.create(name="female")
        self.age = Age.objects.create(name="Adult", min_age=20, max_age=40)
        self.season = Season.objects.create(name="Winter")
        self.tag = Tag.objects.create(name="Sale")

    def test_country_serializer(self):
        serializer = CountrySerializer(self.country)
        data = serializer.data
        self.assertEqual(data["name"], "Canada")
        self.assertEqual(data["slug"], "canada")

    def test_color_serializer(self):
        serializer = ColorSerializer(self.color)
        data = serializer.data
        self.assertEqual(data["name"], "Blue")
        self.assertEqual(data["color"], "#0000FF")

    def test_gender_serializer(self):
        serializer = GenderSerializer(self.gender)
        data = serializer.data
        self.assertEqual(data["name"], "female")

    def test_age_serializer(self):
        serializer = AgeSerializer(self.age)
        data = serializer.data
        self.assertEqual(data["min_age"], 20)
        self.assertEqual(data["max_age"], 40)

    def test_season_serializer(self):
        serializer = SeasonSerializer(self.season)
        data = serializer.data
        self.assertEqual(data["name"], "Winter")

    def test_tag_serializer(self):
        serializer = TagSerializer(self.tag)
        data = serializer.data
        self.assertEqual(data["name"], "Sale")


class AttributesViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

        self.role = Role.objects.create(name="Manager")
        self.admin_user = User.objects.create_user(username="admin", password="pass", is_staff=True, role=self.role)
        self.normal_user = User.objects.create_user(username="user", password="pass", is_staff=False, role=self.role)

        self.country = Country.objects.create(name="France")
        self.color = Color.objects.create(name="Green", color="#00FF00")

        self.country_list_url = reverse("country_list")
        self.country_detail_url = reverse("country_detail", args=[self.country.pk])
        self.color_list_url = reverse("color_list")
        self.color_detail_url = reverse("color_detail", args=[self.color.pk])

    def test_country_list_view_get(self):
        response = self.client.get(self.country_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("France", [c["name"] for c in response.data])

    def test_country_create_view_admin_only(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(self.country_list_url, {"name": "Germany"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.country_list_url, {"name": "Germany"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["slug"], "germany")

    def test_country_detail_update_permission(self):
        data = {"name": "France Updated"}

        self.client.force_authenticate(user=self.normal_user)
        response = self.client.patch(self.country_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.patch(self.country_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "France Updated")

    def test_color_detail_delete_permission(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(self.color_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.color_detail_url)
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
