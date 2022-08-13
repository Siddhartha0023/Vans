from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cart/', views.cart, name = 'cart'),
    # path('account/', views.account, name = 'account'),
    path('products/', views.products, name = 'products'),
    path('details/', views.details, name = 'details'),


]