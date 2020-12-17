from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """

    products = Product.objects.filter(category=17)
    billabong = Product.objects.filter(brand='Billabong')

    print(billabong)

    context = {
        'products': products,
        'billabong': billabong,
    }

    return render(request, 'home/index.html', context)
