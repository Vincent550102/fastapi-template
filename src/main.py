from typing import Optional, Union
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from contextlib import asynccontextmanager
from routers import message
# from pymongo import MongoClient
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    # mongo_username = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'root')
    # mongo_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'example')
    # app.state.db = MongoClient(
    #     f'mongodb://{mongo_username}:{mongo_password}@mongo:27017').magazine
    # print("connected to mongodb")
    app.state.db = None
    print("started")
    yield
    print("ended")


def get_db(app: FastAPI):
    return app.state.db


app = FastAPI(lifespan=lifespan)  # 建立一個 Fast API application


@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    return {"Hello": "World"}


app.include_router(message.router)
