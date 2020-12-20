from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    message: str = Field(title="Message to be sent")
