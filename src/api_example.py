import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import runner


class Code(BaseModel):
    code : str
    language : str


app = FastAPI()


@app.get("/")
async def home():
    return "Hello There"

@app.post("/api/run")
async def run_the_code(code : Code):
    output = await runner.run_code(repr(code.code), code.language, await_task=True)
    return {"output":output}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)