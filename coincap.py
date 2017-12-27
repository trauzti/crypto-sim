import sys
import datetime
import requests
import json

dollar_amount = 100
coin_amount = 0
print "Initial amount: $%f" % dollar_amount

x = requests.get("http://coincap.io/history/30day/%s" % sys.argv[1])
print x.text
z = json.loads(x.text)
prices = z["price"]
latest_price = None
for item in prices:
    ts = item[0]
    price = item[1]
    tsdt = datetime.datetime.fromtimestamp(ts/1000)
    print tsdt,price
    latest_price = price
    if coin_amount == 0:
        coin_amount = dollar_amount / float(price)

coin_amount = dollar_amount / float(price)

print "Final amount: $%f" % (latest_price * coin_amount)


