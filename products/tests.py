from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from categories.models import Category
from brands.models import Brand
from companies.models import Company
from attributes.models import Color, Gender, Age, Season, Country, Tag
from accounts.models import User, Role
from .models import Product


class ProductModelsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Shoes")
        self.brand = Brand.objects.create(name="Nike")
        self.company = Company.objects.create(name="NikeCo")
        self.color = Color.objects.create(name="Red")
        self.gender = Gender.objects.create(name="Male")
        self.age = Age.objects.create(name="Adult", min_age=18, max_age=64)
        self.season = Season.objects.create(name="Winter")
        self.country = Country.objects.create(name="USA")
        self.tag1 = Tag.objects.create(name="Sport")
        self.tag2 = Tag.objects.create(name="Casual")

    def test_product_str(self):
        product = Product.objects.create(
            name="Air Max",
            rating=5,
            price=200,
            category=self.category,
            brand=self.brand,
            company=self.company,
            color=self.color,
            gender=self.gender,
            age=self.age,
            season=self.season,
            country=self.country
        )
        product.tags.add(self.tag1, self.tag2)
        self.assertEqual(str(product), "Air Max")


class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.role = Role.objects.create(name="admin")
        self.admin_user = User.objects.create_user(
            username="adminuser", password="password123", role=self.role, is_staff=True
        )
        self.normal_user = User.objects.create_user(username="normaluser", password="password123")

        self.category = Category.objects.create(name="Shoes")
        self.brand = Brand.objects.create(name="Nike")
        self.company = Company.objects.create(name="NikeCo")
        self.color = Color.objects.create(name="Red")
        self.gender = Gender.objects.create(name="Male")
        self.age = Age.objects.create(name="Adult", min_age=18, max_age=64)
        self.season = Season.objects.create(name="Winter")
        self.country = Country.objects.create(name="USA")
        self.tag1 = Tag.objects.create(name="Sport")
        self.tag2 = Tag.objects.create(name="Casual")

        self.product = Product.objects.create(
            name="Air Max",
            rating=4,
            price=150,
            category=self.category,
            brand=self.brand,
            company=self.company,
            color=self.color,
            gender=self.gender,
            age=self.age,
            season=self.season,
            country=self.country
        )
        self.product.tags.add(self.tag1)

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Air Max", [p["name"] for p in response.data])

    def test_product_create_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        data = {
            "name": "Zoom Fly",
            "rating": 5,
            "price": 180,
            "category": self.category.id,
            "brand": self.brand.id,
            "company": self.company.id,
            "color": self.color.id,
            "gender": self.gender.id,
            "age": self.age.id,
            "season": self.season.id,
            "country": self.country.id,
            "tags": [self.tag1.id, self.tag2.id]
        }
        response = self.client.post(reverse("product_list"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Zoom Fly")

    def test_product_create_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        data = {"name": "Zoom Fly", "rating": 5, "price": 180}
        response = self.client.post(reverse("product_list"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_detail_view(self):
        response = self.client.get(reverse("product_detail", args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Air Max")

    def test_product_update_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.patch(reverse("product_detail", args=[self.product.id]), {"price": 160}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], 160)

    def test_product_update_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.patch(reverse("product_detail", args=[self.product.id]), {"price": 160}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_delete_view_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(reverse("product_detail", args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_product_delete_view_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(reverse("product_detail", args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_filter_min_max_price(self):
        Product.objects.create(
            name="Budget Shoe",
            rating=3,
            price=50,
            category=self.category,
            brand=self.brand,
            company=self.company,
            color=self.color,
            gender=self.gender,
            age=self.age,
            season=self.season,
            country=self.country
        )
        response = self.client.get(reverse("product_list") + "?min_price=100&max_price=200")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(100 <= p["price"] <= 200 for p in response.data))
