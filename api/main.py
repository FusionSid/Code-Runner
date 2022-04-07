from fastapi import FastAPI
from runner import runner_endpoint
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return "Hello There"


app.include_router(runner_endpoint)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)