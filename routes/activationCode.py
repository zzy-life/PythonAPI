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
    eval: list[Body] = []
    for record in strData:
        # 使用 parse_obj 方法将数据库记录转换为 Body 实例
        # 确保 record 是一个字典，且键名与数据库列名一致
        body_instance = Body.parse_obj(record)
        eval.append(body_instance)

    evals = UserResponseBody(
        code=200,
        msg="Success",
        data=eval,
    )

    return evals
