import uuid
from django.utils import timezone
from django.db import models


class CryptoCurrency(models.Model):
    """ 
        We pull data on this from CoinmarketCap API
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cmc_id = models.IntegerField()  # CoinMarketCap ID
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PriceListing(models.Model):
    """ 
        Class for the Price Listings
    """
    currency = models.ForeignKey(
        'CryptoCurrency', related_name='ctypto_price', on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    btc = models.DecimalField(max_digits=100, decimal_places=10, null=True)
    usd = models.DecimalField(max_digits=100, decimal_places=4, null=True)
    market_cap = models.DecimalField(max_digits=100, decimal_places=1, null=True)
    daily_volume = models.IntegerField(null=True)
    percent_change_1h = models.IntegerField(default=0, null=True)
    percent_change_24h = models.IntegerField(default=0, null=True)
    percent_change_7d = models.IntegerField(default=0, null=True)
    max_supply = models.DecimalField(max_digits=100, decimal_places=1, default=0, null=True)
    circulating_supply = models.DecimalField(max_digits=100, decimal_places=1, default=0, null=True)
