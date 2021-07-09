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
        'stripe_public_key': 'pk_test_51JBGU9I5Jb6HSSk6B8EgzY9SVw1Ne9GCeHEzWgkG7riLah0QQ9pRV02hX0UAeB8Rx7oxknslUip8iXY5t4SVrCqG00pnJraVuQ',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)