# -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{id}")
def user(id):
    return {"id": id}