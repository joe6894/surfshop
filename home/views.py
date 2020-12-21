from django.shortcuts import render, redirect, reverse
from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """

    products = Product.objects.filter(category=17)

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)

def billabong(request):

    products = Product.objects.filter(brand='Billabong')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def animal(request):

    products = Product.objects.filter(brand='Animal')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def oneill(request):

    products = Product.objects.filter(brand="O'neill")

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def gul(request):

    products = Product.objects.filter(brand='Gul')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


