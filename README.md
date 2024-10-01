# Hub de APIs

Para diferentes "APPs" ou programas, com contexto de namespace próprio, gerenciado pelo FastAPI mas independente entre sí.

## Instalação
```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Iniciando servidor das aplicações:

```sh
uvicorn main:main_app --reload
ctrl+c -> para encerrar o servidor da aplicação 
```
## Estrutura
```sh
api_hub/
│
├── openweather_app/
│   ├── __init__.py
│   ├── main.py
│
├── polygon_app/
│   ├── __init__.py
│   ├── main.py
│
├── .env
├── .gitignore
├── estrutura.sh
├── main.py
├── README.md
└── requirements.txt
```

## Módulos



| Arquivo | Descrição |
| ------ | ------ |
| --- | --- |
| --- | --- |
| --- | --- |
| --- | --- |
| --- | --- |
| --- | --- |
