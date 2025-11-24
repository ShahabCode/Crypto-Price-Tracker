import requests, pymongo

try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print("Connected to Database!")
except Exception as e:
    print(f"Failed to connect to Database: {e}")

mydb = client["CryptoDB"]
myCollection = mydb["CryptoCL"]

req = requests.get("https://api.tgju.org/v1/market/dataservice/crypto-assets?category=&type=overview&start=0&length=100").json()

for item in req["data"]:
    name = item["symbol"]
    price = item["p"]
    price_irr = item["p_irr"]
    
    existing = myCollection.find_one({"Name": name})

    if existing:
        update_fields = {}
        if existing.get("Price") != price:
            update_fields["Price"] = price
        if existing.get("Price_irr") != price_irr:
            update_fields["Price_irr"] = price_irr

        if update_fields:
            myCollection.update_one({"Name": name}, {"$set": update_fields})
    else:
        mydict = {"Name": name, "Price": price, "Price_irr": price_irr}
        myCollection.insert_one(mydict)
