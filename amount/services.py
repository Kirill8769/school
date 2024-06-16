import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_stripe_price(amount, course):
    """Создаёт цену в страйпе."""

    price = stripe.Price.create(
      currency='rub',
      unit_amount=amount * 100,
      product_data={'name': f'Оплата курса {course}'},
    )
    return price


def create_stripe_session(price):
    """Создаёт сессию на оплату в страйпе."""

    session = stripe.checkout.Session.create(
      success_url='http://127.0.0.1:8000/amounts/success',
      line_items=[{'price': price.get('id'), 'quantity': 1}],
      mode='payment',
    )
    return session
