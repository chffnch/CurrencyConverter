import requests
import json

ccy_from = input("Currency from: ").lower()

# Retrieve exchange rates for EUR and USD from the online source
r = requests.get('http://www.floatrates.com/daily/eur.json')

cache = dict()
cache["eur"] = json.loads(requests.get('http://www.floatrates.com/daily/eur.json').text)
cache["usd"] = json.loads(requests.get('http://www.floatrates.com/daily/usd.json').text)

while True:
    ccy_to = input("Currency to: ").lower()
    
    if ccy_to == "":
        print("End of session.")
        break
    amt_ccy_from = float(input("Amount currency from: "))
    print("Checking the cache...")
    
    try:
        cache[ccy_to]
        print("Oh! It is in the cache!")
    except KeyError:
        print("Sorry, but it is not in the cache!")
        cache[ccy_to] = json.loads(requests.get(f'http://www.floatrates.com/daily/{ccy_to}.json').text)
    
    amt_ccy_to = round(amt_ccy_from * cache[ccy_to][ccy_from]['inverseRate'], 2)
    print(f"You received {amt_ccy_to} {ccy_to.upper()}.")

