from fastapi import FastAPI
import pymongo

try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print("Connected to Database!")
except Exception as e:
    print(f"Failed to connect to Database: {e}")

mydb = client["CryptoDB"]
myCollection = mydb["CryptoCL"]


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Welcome to Crypto Price API!",

        "routes": {
            "/crypto?name=BTC": "Get price of a specific cryptocurrency",
            "/top100": "Get top 100 cryptocurrencies sorted by price",
            "/": "You are here! API usage guide."
        },

        "examples": {
            "Single crypto": "http://127.0.0.1:8000/crypto?name=BTC",
            "Top 100 cryptos": "http://127.0.0.1:8000/top100"
        },

        "note": "Parameter 'name' must be the symbol of cryptocurrency (e.g., BTC, ETH, DOGE)."
    }


@app.get("/crypto")
async def crypto(name: str | None=None):
    name = name.upper()
    if myCollection.find_one({"Name": name}):
        price = myCollection.find_one({"Name": name})["Price"]
        price_irr = myCollection.find_one({"Name": name})["Price_irr"]
        return{"Price": price, "Price_irr": price_irr}
    else:
        return{"Crypto Name is not Exist!"}
    

@app.get("/top100")
async def top_100():
    items = list(myCollection.find())

    for item in items:
        try:
            item["Price_num"] = float(str(item["Price"]).replace(",", "").replace(" ", "").replace("٬", ""))
        except:
            item["Price_num"] = 0

    items.sort(key=lambda x: x["Price_num"], reverse=True)

    top_items = items[:100]

    for item in top_items:
        item["_id"] = str(item["_id"])

    return {"Top100": top_items}
