from model import FinanceInput, DateModel
from utils import extract_arguments, extract_value


new_finance_args_map = {
    "-v": "value",
    "-dc": "description",
    "-d": "date",
    "-t": "type",
}


def parse_new_finance_arguments(arguments: tuple) -> FinanceInput:
    resp_args = extract_arguments(arguments)

    data = {}
    for _key, _value in resp_args:
        key_name = new_finance_args_map[_key]
        data[key_name] = _value

    data = FinanceInput(**data)
    return data


def parse_date_arguments(arguments: tuple) -> DateModel:
    value = extract_value(arguments)

    data = DateModel(start=value, end=value)
    return data
