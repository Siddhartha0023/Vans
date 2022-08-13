
from http import client
from urllib import response
from django.urls import resolve, reverse
from django.test import SimpleTestCase, TestCase
from store.views import cart, products, details, index



# url testing
class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        print(url)
        self.assertEquals(resolve(url).func,index)

    def test_index_url(self):
        url = reverse('cart')
        print(url)
        self.assertEquals(resolve(url).func,cart)


    def test_index_url(self):
        url = reverse('products')
        print(url)
        self.assertEquals(resolve(url).func,products)

    def test_index_url(self):
        url = reverse('details')
        print(url)
        self.assertEquals(resolve(url).func,details)


    
    # CRU testing    

from django.test import  TestCase,Client,SimpleTestCase
from django.contrib.auth.models import User
from store.views import index
from store.models import Customer

#create your test here

class testviews(TestCase):
    def test_index(self):
        user = User.objects.create(username='siddhartha')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='siddhartha', password='12345')
        response=client.get(reverse(index))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'index.html')


    def test_create(self):
        user = User.objects.create(username='siddahrtha')
        user.set_password('12345')
        user.save()
        client=Client()
        logged_in = client.login(username='siddhartha', password='12345')
        response=client.get(reverse('customer_create'),{
            
        })
