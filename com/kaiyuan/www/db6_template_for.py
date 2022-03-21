# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse # 重定向
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("../../../static/pages")

todos = ["写日记", "看电影", "学习"]

@app.get("/")
def index(req: Request):
    return template.TemplateResponse("index.html", context={"request": req, "todos": todos})

@app.post("/todo")
def todo(todo=Form(None)):
    """处理用户发过来的 todolist 数据"""
    todos.insert(0, todo)
    return RedirectResponse("/", status_code=302)