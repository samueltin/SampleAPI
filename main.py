# Sample FastAPI app (main.py)
from fastapi import FastAPI
app = FastAPI()

@app.get("/claims")
def read_claims():
    return {"message": "You are authorized"}

