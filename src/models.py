from pydantic import BaseModel, validator
from typing import List, Union
from datetime import datetime


class MessageModule(BaseModel):
    status: str
    message: str
    created_at: int


class ErrorMessage(BaseModel):
    detail: str
