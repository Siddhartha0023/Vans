from django.urls import resolve, reverse
from django.test import SimpleTestCase, TestCase
from user.views import login, register, logout


class  TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('login')
        print(url)
        self.assertEquals(resolve(url).func,login)
    
    def test_index_url(self):
        url = reverse('register')
        print(url)
        self.assertEquals(resolve(url).func,register)

    # def test_index_url(self):
    #     url = reverse('logout')
    #     print(url)
    #     self.assertEquals(resolve(url).func,logout)