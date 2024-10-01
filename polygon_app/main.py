from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

app = FastAPI()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

@app.get("/stock/{symbol}/{date}")
async def get_stock_data(symbol: str, date: str):
    url = f"https://api.polygon.io/v1/open-close/{symbol}/{date}?adjusted=true&apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    return response.json()
