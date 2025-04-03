import stripe

from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates


stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(rub_price):
    """Конвертирует рубли в доллары."""

    usd_price = rub_price * 83
    return usd_price


def create_stripe_product(product_name):
    """Создаем stripe продукт"""
    stripe_product = stripe.Product.create(name=product_name)
    return stripe_product


def create_stripe_price(product_name, amount):
    """Создает цену в docs.stripe.com."""

    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product_name},
    )


def create_stripe_session(price):
    """Создает сессию на оплату в docs.stripe.com."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/lms/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
