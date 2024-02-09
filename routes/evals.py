import os
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Eval(BaseModel):
    input: str
    output: str


@router.get("/evals")
async def get_evals():

    evals: list[Eval] = []
    evals.append(
            Eval(
                input="help(object)",
                output="help",
            )
        )
   
    return evals
