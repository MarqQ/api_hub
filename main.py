from fastapi import FastAPI
from openweather_app.main import app as openweather_app
from polygon_app.main import app as polygon_app

main_app = FastAPI()

# Incluindo as rotas da aplicação OpenWeather
main_app.mount("/openweather", openweather_app)

# Incluindo as rotas da aplicação Polygon
main_app.mount("/polygon", polygon_app)
