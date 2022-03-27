# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request
# 引入这个模板引擎,用于解析html文件内容
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

# 将app实例和数据库绑定在一起
from tortoise.contrib.fastapi import register_tortoise



app = FastAPI()
template = Jinja2Templates("../../../static/pages")

# 数据库绑定
register_tortoise(app,
                  db_url="mysql://root:123456@localhost:3306/fastapi",
                  modules={"models": []},
                  generate_schemas=True,
                  add_exception_handlers=True)

@app.get("/")
def user(username, req: Request):
    """返回一个html文件,需要现有解析引擎,模板引擎"""
    # context=必须加上去的,而且不能进行修改,"request": req,也不能修改
    return template.TemplateResponse("index.html", context={"request": req, "name": username})