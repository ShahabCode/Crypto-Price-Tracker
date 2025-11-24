import requests, pymongo, time  

def fetch_all_crypto():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017")
        print("Connected to Database!")
    except Exception as e:
        print(f"Failed to connect to Database: {e}")
        return

    mydb = client["CryptoDB"]
    myCollection = mydb["CryptoCL"]

    start = 0
    length = 100

    while True:
        url = f"https://api.tgju.org/v1/market/dataservice/crypto-assets?category=&type=overview&start={start}&length={length}"
        req = requests.get(url).json()

        data = req.get("data", [])
        if not data:  
            print("All data fetched!")
            break

        for item in data:
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

        print(f"Fetched {len(data)} items starting from {start}")
        start += length  
        time.sleep(1)  
        
fetch_all_crypto()