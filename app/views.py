from django.shortcuts import render

# Create your views here.
def home(req):
    import requests
    import json
    
    # price requests
    price_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,BSV,USDT,LTC,EOS,BNB,ADA&tsyms=USD")
    price = json.loads(price_req.content)
    
    
    # new requests
    api_req = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_req.content)
    return render(req, "home.html", {"api": api, "price": price})
