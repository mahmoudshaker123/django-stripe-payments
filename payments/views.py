import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutView(View):
    def post(self, request):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 2000,  # 20.00$
                    'product_data': {
                        'name': 'Test Product',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )
        return redirect(session.url)

def success_view(request):
    return render(request, 'payments/success.html')

def cancel_view(request):
    return render(request, 'payments/cancel.html')
    

