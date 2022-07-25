from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="login")
def index(request):
    return render(request, 'index.html')

@login_required(login_url="login")
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url="login")
def account(request):
    return render(request, 'account.html')

@login_required(login_url="login")
def products(request):
    return render(request, 'products.html')

@login_required(login_url="login")
def details(request):
    return render(request, 'details.html')

