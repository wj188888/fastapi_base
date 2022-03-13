# -*- coding: utf-8 -*-

# 导入fastapi包
import uvicorn
from fastapi import FastAPI

app = FastAPI()
# 添加首页
@app.get("/")
def index():
    """添加首页"""
    return "This is Home Page"

@app.get("/users")
def users():
    """获取用户列表,这个接口返回字典内容"""
    return {"mag": "Get all users", "code": 2001}

@app.get("/projects")
def projects():
    """获取项目列表,这个接口返回列表内容"""
    return ["项目一", "生产环境项目", "测试项目"]


if __name__ == '__main__':

    uvicorn.run(app)