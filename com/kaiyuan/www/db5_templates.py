# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request
# 引入这个模板引擎,用于解析html文件内容
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("../../../static/pages")


@app.get("/")
def user(username, req: Request):
    """返回一个html文件,需要现有解析引擎,模板引擎"""
    # context=必须加上去的,而且不能进行修改
    return template.TemplateResponse("index.html", context={"request": req, "name": username})