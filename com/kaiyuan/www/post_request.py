# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.post("/login")
def login():
    return {"msg": "login success"}

# if __name__ == '__main__':
#     uvicorn.run(app)