from fastapi import Body, FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class DesignationEnum(str, Enum):
    SFW = 'SFW'
    NSFW = 'NSFW'

class OrderEnum(str, Enum):
    Intro = 'Intro'
    Scapegoat = 'Scapegoat'
    Delay = 'Delay'

class ExcusePart(BaseModel):
    content: str
    designation: DesignationEnum
    order: OrderEnum = 'NSFW'


@app.get("/")
def root():
    return {"message": "This is the rooute"}


@app.post("/excuses")
def create_excuse(part_of_excuse: ExcusePart):
    print(part_of_excuse.content)
    print(part_of_excuse.designation)
    print(part_of_excuse.order)
    return {"new_excuse": part_of_excuse.dict()}