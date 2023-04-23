from pydantic import BaseModel, validator
from datetime import datetime
from enum import Enum


def gen_datetime(
    day=datetime.today().day,
    month=datetime.today().month,
    year=datetime.today().year,
    hour=0,
    minute=0,
    second=0,
    microsecond=0,
    first_hour=False,
):
    if first_hour:
        hour = 1
        minute = 1
        second = 1
        microsecond = 1

    return datetime(
        day=day,
        month=month,
        year=year,
        hour=hour,
        minute=minute,
        second=second,
        microsecond=microsecond,
    )


class DateModel(BaseModel):
    start: datetime = gen_datetime(first_hour=True)
    end: datetime = gen_datetime()

    @validator("start", pre=True)
    def start_date_pre_trait(cls, value: str):
        """
        Allow uses like:
        'dd/mm/YY'
        or 'dd/mm'
        or even 'dd'
        """
        d = list(map(int, value.split("/")))

        if len(d) == 3:
            return gen_datetime(day=d[0], month=d[1], year=d[2], first_hour=True)
        if len(d) == 2:
            return gen_datetime(day=d[0], month=d[1], first_hour=True)
        if len(d) == 1:
            return gen_datetime(day=d[0], first_hour=True)
        return value

    @validator("end", pre=True)
    def end_date_pre_trait(cls, value: str):
        """
        Allow uses like:
        'dd/mm/YY'
        or 'dd/mm'
        or even 'dd'
        """
        d = list(map(int, value.split("/")))

        if len(d) == 3:
            return gen_datetime(day=d[0], month=d[1], year=d[2])
        if len(d) == 2:
            return gen_datetime(day=d[0], month=d[1])
        if len(d) == 1:
            return gen_datetime(day=d[0])
        return value


class TypeEnum(str, Enum):
    spent = "spent"
    receipt = "receipt"


class FinanceInput(BaseModel):
    description: str = ""
    value: float = 0.0
    type: TypeEnum = TypeEnum.spent
    date: datetime = datetime.today()

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
