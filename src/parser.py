from model import FinanceInput
from utils import extract_arguments


names_dict = {
    "-v": "value",
    "-dc": "description",
    "-d": "date",
    "-t": "type",
}

def parse_new_finance_arguments(arguments: tuple) -> FinanceInput:
    options = extract_arguments(arguments)

    data = {}
    for _key, _value in options:
        key_name = names_dict[_key]
        data[key_name] = _value

    data = FinanceInput(**data)
    return data