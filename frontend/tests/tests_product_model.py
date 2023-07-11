from itertools import product
from django.test import TestCase
from faker import Faker
from datetime import datetime as dt

from frontend.models import Category, Product


class TestProductModel(TestCase):
    def test_add_product(self):
        f = Faker()
        c = Category.objects.create()
        c.category_name = "fruta"
        c.save()
        p = Product.objects.create(
            product_name="uva",
            category_id=c.id,
            expire_date=dt.now().date(),
            units=265,
        )
        p.save()
        try:
            self.assertEqual(p, Product.objects.get(pk=p.id))
        except Product.DoesNotExist:
            raise Product.DoesNotExist()
