from pydantic import BaseModel


class DocumentCreate(BaseModel):
    text: str
    summary: str = ""
    url: str = ""


class DocumentRead(BaseModel):
    summary: str
    url: str = ""
    id: int

    class Config:
        orm_mode = True