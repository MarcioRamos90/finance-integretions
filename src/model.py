from pydantic import BaseModel, validator
import datetime
from enum import Enum


class TypeEnum(str, Enum):
    spent = 'spent'
    receipt = 'receipt'


class FinanceInput(BaseModel):
    description: str = ""
    value: float = 0.0
    type: TypeEnum = TypeEnum.spent
    date: datetime.date = datetime.date.today()

    @validator("type", pre=True)
    def type_pre_trait(cls, value):
        if value == "+":
            return TypeEnum.receipt
        elif value == "-":
            return TypeEnum.spent
        return value

    @validator("value", pre=True)
    def value_pre_trait(cls, value):
        if type(value) is str:
            return value.replace(",", ".")
        return value
