from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from typing import Generic, TypeVar, Optional

# 定义一个泛型变量 T，它将用于表示不同的数据类型
T = TypeVar('T')

# 定义一个带有泛型数据字段的响应体基类
class ResponseBody(GenericModel, Generic[T]):
    code: int = Field(..., description="状态码")
    msg: str = Field(..., description="消息")
    data: Optional[T] = Field(None, description="数据载荷")