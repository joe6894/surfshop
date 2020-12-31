from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import UserWishlist
from profiles.models import UserProfile


# view to load wishlist
@login_required
def view_wishlist(request):
    """ A view to return the wishlist """
    user = UserProfile.objects.get(user=request.user)
    wishlist = Product.objects.filter(userwishlists__user_profile=user)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'wishlist/wishlist.html', context)


# A view that allows users to add to their wishlist
@login_required
def add_wish(request, product_id):
    """
    Allows users to add or remove a product to/from their personal wishlist.\n
    """

    wish = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    wishlist_user, created = UserWishlist.objects.\
        get_or_create(user_profile=user)
    wishlist = Product.objects.filter(userwishlists__user_profile=user)

    if created:
        wish.userwishlists.add(wishlist_user.id)
    else:
        if wish in wishlist:
            wish.userwishlists.remove(wishlist_user.id)
            messages.info(request, "Successfully removed from your wishlist")

        else:
            wish.userwishlists.add(wishlist_user.id)
            messages.info(request, "Successfully added to your wishlist")

    return redirect(reverse('wishlist'))
