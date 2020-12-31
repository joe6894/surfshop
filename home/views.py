from django.shortcuts import render, redirect, reverse
from products.models import Product

# Create your views here.


# View for home page
def index(request):
    """ A view to return the index page """

    products = Product.objects.filter(category=17)

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


# View to load all billabong products
def billabong(request):

    products = Product.objects.filter(brand='Billabong')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# View to load all animal products
def animal(request):

    products = Product.objects.filter(brand='Animal')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# view to load o'neill products
def oneill(request):

    products = Product.objects.filter(brand="O'neill")

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# view to load all gul products
def gul(request):

    products = Product.objects.filter(brand='Gul')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
