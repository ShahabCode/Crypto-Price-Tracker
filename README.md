# 🚀 Crypto Price Tracker

A simple Python project that fetches **real-time cryptocurrency prices** from a public API and stores them in **MongoDB**.  
This project also provides a **FastAPI** endpoint so you can query stored crypto prices easily.

---

## 📌 Features

- Fetches crypto prices from a public API  
- Stores or updates data in MongoDB  
- Provides API endpoints using FastAPI  
- Shows the top 100 cryptocurrencies sorted by price  

---

## 🗂️ Project Structure

```
├── main.py       # Fetch & save crypto prices into MongoDB
├── api.py        # FastAPI server to access saved data
└── README.md
```

---

## ⚙️ Requirements

Make sure you have these installed:

- Python 3.10+
- MongoDB installed & running locally
- Required Python packages:

```
pip install requests pymongo fastapi uvicorn
```

---

## ▶️ Running the Project

### 1. Start MongoDB  
Ensure MongoDB is running on:

```
mongodb://localhost:27017
```

### 2. Run the data fetcher:

```
python main.py
```

### 3. Start the FastAPI server:

```
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

---

## 🌐 API Usage Guide

### **Base URL**

```
http://127.0.0.1:8000/
```

---

### 📍 **1. Get Instructions**

```
GET /
```

Returns a simple guide on how to use the API.

---

### 📍 **2. Get Price of a Specific Crypto**

```
GET /crypto?name=BTC
```

Example Response:

```json
{
  "Price": "92000",
  "Price_irr": "5500000000"
}
```

---

### 📍 **3. Get Top 100 Cryptos**

```
GET /top100
```

Example Response:

```json
[
  {
    "Name": "BTC",
    "Price": 92000
  },
  {
    "Name": "ETH",
    "Price": 4800
  }
]
```

---

## 📝 Notes

- Data is refreshed when you run `main.py`
- API works only with the data stored in MongoDB
- The `top100` route sorts cryptos by price (descending)

---

## ⭐ Contribute

Feel free to open issues or suggest improvements.



