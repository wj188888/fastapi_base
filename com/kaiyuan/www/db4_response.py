# -*- coding: utf-8 -*-

from fastapi import FastAPI, Header, Body, Form
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse


app = FastAPI()

@app.get("/user")
def user():
    """JSONResponse继承之reponses,有5-6个参数"""
    return JSONResponse(content={"msg": "get user"},
                        status_code= 202,
                        headers= {"Token": "wangjie"})

@app.get("/")
def user():
    """返回html内容"""
    html_content = """
    <html>
        <body>
            <p style="color:gold">欢迎来到FastAPI!</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/image")
def user():
    """返回图片内容"""
    image_path = "../../../static/28years.png"
    # 没有filename参数,那么就会直接打开这个文件图片
    return FileResponse(image_path, filename="wj.png")

@app.get("/txt")
def user():
    """这个之查看文件内容,不进行下载"""
    txt_path = "../../../static/biji"
    return FileResponse(txt_path)