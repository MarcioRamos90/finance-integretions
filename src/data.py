import datetime

from firebase_admin import firestore
from arg_handler import parse_new_finance_arguments, parse_date_arguments

from setup import COLLECTION_NAME
from model import FinanceInput


async def get_list_by_day(*args):
    db = firestore.client()

    data_parsed = parse_date_arguments(args)
    
    users_ref = db.collection(COLLECTION_NAME)
    docs = users_ref.stream()

    list_items = ""
    _sum = 0
    for doc in docs:
        item = doc.to_dict()
        desc = item.get("description")
        value = item.get("value")
        datetime_with_nanoseconds = item.get("date")
        date = datetime.datetime.fromtimestamp(datetime_with_nanoseconds.timestamp())

        print(data_parsed.start, "(", date, ")", data_parsed.end)
        if date.date() >= data_parsed.start.date() and date.date() <= data_parsed.end.date() :
            list_items += f"{desc}\t\t{value}\t\t{date}\n"
            _sum += value
    list_items += f"\ntotal:\t\t{_sum}"
    return list_items
    


async def get_all_finances(*args):
    db = firestore.client()

    users_ref = db.collection(COLLECTION_NAME)
    docs = users_ref.stream()

    soma = 0
    for doc in docs:
        valores = doc.to_dict()
        soma += valores.get("valor")
    return soma


async def new_finance_item(*args):
    try:
        data_parsed: FinanceInput = parse_new_finance_arguments(args)

        db = firestore.client()
        data = data_parsed.dict()
        data["date"] = datetime.datetime.fromordinal(data["date"].toordinal())

        new_finance_ref = db.collection(COLLECTION_NAME).document()
        new_finance_ref.set(data)

        return "Created!"
    except Exception as ex:
        return str(ex)
