python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:main_app --reload