from pydantic import BaseModel


class Detail(BaseModel):
    detail: str


class ResponseModel(BaseModel):
    class Config():
        orm_mode = True
