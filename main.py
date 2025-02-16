from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/database")
async def get_database_url():
    db_url = os.getenv('DATABASE_URL')
    print('******************************************************')
    print(f'DATABASE_URL: {db_url}')
    print('******************************************************')
    return {
        "data": db_url
    }
