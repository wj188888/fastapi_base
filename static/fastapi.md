# FastApi

## 和Django以及flask区别
是支持原生的异步编程的,python异步编程或多或少是有兼容性问题

## Fastapi可以用来干什么?
- 开发 Web API
- 开发网站
- 做一个测试平台
- 做一个测试平台
- 做一个持续集成工具
- 生成文档

## 为什么要学习fastapi?
- FastApi 的使用方法和设计参考了即使个python明星项目,博彩众长
- FastAPI和Flask 一样简约
- FastAPI 非常新,并且基于python3.6 的类型声明系统
- 自动生成文档
- 类型声明和数据检验
- 内置身份认证
- 性能强
- 原生支持异步
- 强大的依赖注入系统
- GraphQL和Websocket

## 安装fastapi
- 第一步:
**python编辑工具:pycharm和vsvode和supply**
**安装fastapi技巧,是就是pip install fastapi[all] 会安装很多fastapi依赖的插件**
**最小安装,然后其他的包就不会安装了**
- 第二步:
安装服务器(uvicorn是一个性能很强的服务器):
```
pip install uvicorn
# 查看目录下文件的总和
du -sh
```

## 开启服务
```
# 导入fastapi包
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app)

```
第一种方式:
1. 开启服务的方式一:
    - 在main函数直接运行,默认无法选择端口和ip
2. 开启服务的方式二:
    - 在terminal中使用命令运行

```
# 其中quickstart_demo是要运行的文件,然后app是你的实例
uvicorn quickstart_demo:app --reload
# 注意是quickstart_demo没有带.py
```
`--reload 指的是:每次修改源文件,就会在服务器加载`

## 如何返回json数据
```
# 可以是字典,列表,字符串等
@app.get("/projects")
def projects():
    """这个接口返回列表内容"""
    return ["项目一", "生产环境项目", "测试项目"]
```
## 查看docs接口文档
```
访问:
http://127.0.0.1:8000/docs
```
还可以访问另外一种风格的接口文档:
```
http://127.0.0.1:8000/redoc
```