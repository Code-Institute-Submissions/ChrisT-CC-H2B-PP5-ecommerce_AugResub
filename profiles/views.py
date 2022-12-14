""" profiles app views """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """

    # Get current profile from DB
    myprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=myprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=myprofile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'myprofile': myprofile,
    }

    return render(request, template, context)


def orders(request):
    """ Display the user's orders. """
    # Get all products and categories from DB
    all_orders = Order.objects.all()

    template = 'profiles/orders.html'
    context = {
        'all_orders': all_orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display the user's order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        # 'from_profile': True,
    }

    return render(request, template, context)
