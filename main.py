from fastapi import FastAPI
import uvicorn
from openweather_app.main import app as openweather_app
from polygon_app.main import app as polygon_app

main_app = FastAPI()
# uvicorn.run(main_app, host="127.0.0.1", port=1245)

# Incluindo as rotas da aplicação OpenWeather
main_app.mount("/openweather", openweather_app)

# Incluindo as rotas da aplicação Polygon
main_app.mount("/polygon", polygon_app)


# if __name__ == "__main__":
#     uvicorn.run(main_app, host="127.0.0.1", port=5049)
