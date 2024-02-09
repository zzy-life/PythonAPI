from typing import Optional, List
from evals.responseBody import ResponseBody
from fastapi import APIRouter
from evals.db import database
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter()


class Body(BaseModel):
    id: str
    code: str
    activationTime: datetime = Field(..., alias="activation_time")
    activationType: str = Field(..., alias="activation_type")
    activationNumber: int = Field(..., alias="activation_number")


class UserResponseBody(ResponseBody[List["Body"]]):
    pass


class param(BaseModel):
    name: str
    tax: Optional[int] = None


@router.post("/evals")
async def get_evals(item: param):
    query = "SELECT * FROM activation_code"
    strData = await database.fetch_all(query=query)
     # 使用列表推导式简化数据转换，也可以直接返回 strData
    eval = [Body.parse_obj(record) for record in strData]

    evals = UserResponseBody(
        code=200,
        msg="Success",
        data=eval,
    )

    return evals
