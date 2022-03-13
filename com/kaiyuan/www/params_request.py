# -*- coding: utf-8 -*-
from fastapi import FastAPI, Header, Body, Form # 都在这里进行的导入

app = FastAPI()

# @app.get("/user/{id}")
# def user(id):
#     return {"id": id}

# 写成这种形式,那么这个,还是查询字符串的方式的
@app.get("/user")
def user(id, token=Header(None)): # 传递一个token,然后默认值为Header(None)
    return {"id": id, "token": token}

# 第二种方式:通过json 方式进行传递数据
# @app.post("/login")
# def login(data=Body(None)): # 传递一个token,然后默认值为Header(None)
#     return {"data": data}

# 第三种方式；form表单, 需要安装`pip install python-multipart`
@app.post("/login")
def user(username=Form(None), password=Form(None)): # 传递一个token,然后默认值为Header(None)
    return {"data": {"username": username, "password": password}}
