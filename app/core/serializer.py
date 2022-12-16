from rest_framework.serializers import ModelSerializer
from .models import Currency, Exchange

class CurrencySerializer(ModelSerializer):
  class Meta:
    model = Currency
    fields = ['name', 'exchange', 'fee']

class ExchangeSerializer():
  class Meta:
    model = Exchange
    fields = ['fee_amount', 'base_currency_id', 'exchange_currency_id', 'base_amount', 'exchange']