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
    """Создаёт ссылку на оплату."""

    session = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      line_items=[{"price": "price_1MotwRLkdIwHu7ixYcPLm5uZ", "quantity": 1}],
      mode="payment",
    )
    return session
