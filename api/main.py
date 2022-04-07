from fastapi import FastAPI
from runner import runner_endpoint

app = FastAPI()

@app.get("/")
async def home():
    return "Hello There"


app.include_router(runner_endpoint)