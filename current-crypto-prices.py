import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CryptoPrices(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Make the API call to CoinMarketCap
        api_key = 'YOUR_API_KEY'
        endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        params = {
            'start': '1',
            'limit': '10',
            'convert': 'USD',
            'sort': 'market_cap',
            'sort_dir': 'desc'
        }
        headers = {
            'X-CMC_PRO_API_KEY': api_key,
            'Accept': 'application/json'
        }
        response = requests.get(endpoint,
