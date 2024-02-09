from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel
from evals.db import database

router = APIRouter()


class Eval(BaseModel):
    name: str
    tax: str

class Item(BaseModel):
    name: str
    tax: Optional[int] = None


@router.post("/evals")
async def get_evals(item: Item):
    query = "SELECT * FROM activation_code"
    strData =  await database.fetch_all(query=query)
    print(strData)
    evals: list[Eval] = []
    evals.append(
            Eval(
                name=item.name,
                tax=item.tax,
            )
        )
   
    return evals
