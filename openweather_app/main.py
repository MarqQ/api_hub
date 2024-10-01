from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

app = FastAPI()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weather/{city}")
async def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    return response.json()
