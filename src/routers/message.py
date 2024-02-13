from starlette.requests import Request
from models import MessageModule, ErrorMessage
from fastapi import Depends, APIRouter, HTTPException
from typing import Union

router = APIRouter()


def get_db(request: Request):
    return request.app.state.db


@router.get("/message/",
            status_code=200,
            responses={200: {"model": MessageModule},
                       404: {"model": ErrorMessage}},
            tags=["message"],
            summary="Get message",
            description="Get message",
            deprecated=False)
def get_message(message: str,
                db=Depends(get_db)):

    return MessageModule(
        status="success",
        message=message,
        created_at=1707609706
    )
