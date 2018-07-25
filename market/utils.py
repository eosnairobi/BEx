from .models import CryptoCurrency, PriceListing
import requests
import json


def fetch_cryptos():
    url = 'https://api.coinmarketcap.com/v2/listings/'
    """
        {'id': 2898, 'website_slug': 'gonetwork', 'symbol': 'GOT', 'name': 'GoNetwork'}
         id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cmc_id = models.IntegerField()  # CoinMarketCap ID
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10, unique=True)

    """
    cryptos = []
    try:
        r = requests.get(url)
        # Save All Cryptos to DB

        response = json.loads(r.text)
        data = response.get('data')
        for item in data:
            cryptos.append(CryptoCurrency(name=item['name'], cmc_id=item['id'], symbol=item['symbol']))
        CryptoCurrency.objects.bulk_create(cryptos)       
    except Exception as e:
        print(str(e))

