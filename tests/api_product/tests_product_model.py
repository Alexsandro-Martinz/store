from django.test import RequestFactory, TestCase
from faker import Faker
from datetime import datetime as dt
from django.contrib.auth.models import AnonymousUser, User

from frontend.views.views import addProductsView, productsView
from frontend.models import Category, Product

class TestAddProductView(TestCase):
    def setUp(self):
        f = Faker()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=f.name(),
            email=f.email(),
            password=f.password(),
        )
    
    def test_add_product(self):
        c = Category.objects.create(category_name='vegetal')
        c.save()
        context = {
            'product_name': 'banana',
            'units': 390,
            'expire_date': "2022-12-28",
            'category_id': c.id,
            'description': 'é um fruta of course',
        }
        
        request = self.factory.post("/products/add", context)
        request.user = self.user
        response = addProductsView(request)
        
        self.assertEqual(response.status_code, 200)
        
        products = Product.objects.all().filter(product_name=context['product_name'])
        self.assertEqual(products.count(), 1)
        self.assertEquals(products[0].product_name, context['product_name'])
        
        
            
    def test_access_with_anonymousUser(self):
        request = self.factory.get("/product/add")
        request.user = AnonymousUser()
        response = productsView(request)
        self.assertEqual(response.status_code, 302)
    
    def test_access_with_a_user(self):
        request = self.factory.get("/product/add")
        request.user = self.user
        response = productsView(request)
        self.assertEqual(response.status_code, 200)

class TestProductView(TestCase):
    
    def setUp(self):
        f = Faker()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username=f.name(),
            email=f.email(),
            password=f.password(),
        )
    
    def test_access_with_anonymousUser(self):
        request = self.factory.get("/product")
        request.user = AnonymousUser()
        response = productsView(request)
        self.assertEqual(response.status_code, 302)
    
    def test_access_with_a_user(self):
        request = self.factory.get("/product")
        request.user = self.user
        response = productsView(request)
        self.assertEqual(response.status_code, 200)


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