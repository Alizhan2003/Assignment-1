from pycoingecko import CoinGeckoAPI
for l in  CoinGeckoAPI().get_coins_markets(vs_currency='usd', per_page = int(input("enter n:"))):
    print("%(id)s: %(cap)s usd" % {'id': l['id'], 'cap': l['market_cap']})

