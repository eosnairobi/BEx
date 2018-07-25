import json

import requests

from celery import shared_task
from celery.decorators import periodic_task
from celery.schedules import crontab

from django.utils import timezone

from .models import CryptoCurrency, PriceListing
import time


@periodic_task(
    run_every=crontab(minute='*/20'),
    name="fetch_updates",
    ignore_result=True
)
def get_coin_data():
    # Fetch from ticker.
    # Fetch all cmc_ids from DB, loop over each on Ticker Endpoint
    """
        {
            "data": {
                "id": 4, 
                "name": "Terracoin", 
                "symbol": "TRC", 
                "website_slug": "terracoin", 
                "rank": 728, 
                "circulating_supply": 22935396.0, 
                "total_supply": 22935396.0, 
                "max_supply": 42000000.0, 
                "quotes": {
                    "USD": {
                        "price": 0.108582, 
                        "volume_24h": 3519.06, 
                        "market_cap": 2490371.0, 
                        "percent_change_1h": -0.67, 
                        "percent_change_24h": -2.01, 
                        "percent_change_7d": -5.86
                    }
                }, 
                "last_updated": 1531135764
            }, 
            "metadata": {
                "timestamp": 1531135410, 
                "error": null
            }
        }

    """
    response = None
    cryptos = CryptoCurrency.objects.all()
    for crypto in cryptos:
        try:
            r = requests.get(
                'https://api.coinmarketcap.com/v2/ticker/{}'.format(crypto.cmc_id))
            response = (json.loads(r.text))
        except Exception as e:
            print(str(e))
        if response:
            data = response.get('data')

            # Create the PriceListing
            usd = data['quotes']['USD']['price']
            market_cap = data['quotes']['USD']['market_cap']
            daily_volume = data['quotes']['USD']['volume_24h']
            percent_change_1h = data['quotes']['USD']['percent_change_1h']
            percent_change_24h = data['quotes']['USD']['percent_change_24h']
            percent_change_7d = data['quotes']['USD']['percent_change_7d']
            max_supply = data['max_supply']
            circulating_supply = data['circulating_supply']
            p = PriceListing.objects.create(currency=crypto, usd=usd, market_cap=market_cap, daily_volume=daily_volume,
                             percent_change_1h=percent_change_1h, percent_change_24h=percent_change_24h, percent_change_7d=percent_change_7d, circulating_supply=circulating_supply, max_supply=max_supply)

            time.sleep(300) # Dont violate the 30 reqs/minute rule
