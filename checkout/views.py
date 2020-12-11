from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HkSeHKj1yKM9G7Z55aqWBrPVNVtCK0KQchQbw3do0ClQUmWp9Y1tBJeTfukmCYYFu4qgJ7leSLYyltf8T1GLyEO00Ybemn6Xn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
