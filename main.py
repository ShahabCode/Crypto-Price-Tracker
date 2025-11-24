import requests, pymongo

req = requests.get("https://api.tgju.org/v1/market/dataservice/crypto-assets?category=&type=overview&start=0&length=100").json()

for item in req["data"]:
    name = item["symbol"]
    price = item["p"]
    print(f"name is: {name} && price is: {price}")

