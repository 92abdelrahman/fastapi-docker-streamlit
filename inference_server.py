import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Here you can do things such as load your models

@app.get("/")
def read_root(input_text):
    return {f"Hello {input_text}!"}