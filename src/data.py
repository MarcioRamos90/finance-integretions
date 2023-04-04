import datetime

from firebase_admin import firestore
from parser import parse_new_finance_arguments

from setup import COLLECTION_NAME
from model import FinanceInput


async def get_list_by_day(*args):
    db = firestore.client()

    users_ref = db.collection(COLLECTION_NAME)
    docs = users_ref.stream()

    list_items = ""
    _sum = 0
    for doc in docs:
        item = doc.to_dict()
        desc = item.get("description")
        value = item.get("valor")
        list_items += f"{desc} {value}\n"
        _sum += value
    list_items += f"\ntotal: {_sum}"
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
