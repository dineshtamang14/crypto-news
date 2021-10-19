from django.shortcuts import render
import requests
import json

# Create your views here.
def home(req):
    # price requests
    price_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,BSV,USDT,LTC,EOS,BNB,ADA&tsyms=USD")
    price = json.loads(price_req.content)
    
    
    # new requests
    api_req = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_req.content)
    return render(req, "home.html", {"api": api, "price": price})


def prices(req):
    if req.method == 'POST':
        quote = req.POST['quote']
        quote_req = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD')
        price = json.loads(quote_req.content)
        return render(req, 'price.html', {'quote': quote, 'price': price})
    else:
        return render(req, "price.html", {})
