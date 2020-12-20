import os
from pydantic import BaseSettings
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from .schemas import MessageRequest
from http import HTTPStatus
from .services.telegram import Telegram

app = FastAPI()


class Settings(BaseSettings):
    ENVIRONMENT: str

    class Config:
        env_file = ".env"
        case_sensitive = True


origins = [
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/notification", status_code=HTTPStatus.OK)
def notification(
    message: MessageRequest
):
    Telegram(
        token=os.getenv("TELEGRAM_API_ID"),
        chat_id=os.getenv('TELEGRAM_CHAT_ID')
    ).send(message.message)
    return Response(status_code=HTTPStatus.OK)
