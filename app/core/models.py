from django.db import models

# this class allow the addition of new currencies with initial 1000 units in stock
class Currency(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=3)
  exchange = models.FloatField()
  fee = models.FloatField()
  stock = models.FloatField(default=1000)

# this class is to save the info about exchanges
class Exchange(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateField()
  fee_amount = models.FloatField()
  base_currency_id = models.AutoField()
  exchange_currency_id = models.AutoField()
  base_amount = models.FloatField()
  exchange = models.FloatField()
  

