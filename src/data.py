import getopt
from firebase_admin import credentials, initialize_app, firestore, db
from datetime import datetime
from decouple import config

CREDENTIALS = config("GOOGLE_APPLICATION_CREDENTIALS")

cred = credentials.Certificate(CREDENTIALS)

app = initialize_app(cred)


async def get_all_finances(*args):
    print(args)

    db = firestore.client()

    users_ref = db.collection(u"financas")
    docs = users_ref.stream()

    soma = 0
    for doc in docs:
        id = {doc.id}
        valores = doc.to_dict()
        print(valores)
        soma += valores.get("valor")
    return soma


async def new_finance_item(*args):
    try:
        value, day, description, value_type = parse_new_finance_arguments(args)

        db = firestore.client()
        data = {
            u"descricao": description,
            u"valor": value,
            u"tipo": value_type,
            u"data": day,
        }
        new_finance_ref = db.collection(u"financas").document()
        new_finance_ref.set(data)
        return "Criado com sucesso"
    except Exception as ex:
        return str(ex)


if __name__ == "__main__":
    print(new_finance_item())


def parse_new_finance_arguments(arguments: tuple):
    options, args = getopt.getopt(
        arguments[0].split()[1:],
        "v:d:desc:t",
        ["valor=", "dia=", "descricao=", "tipo="],
    )

    value, day, description, value_type = None, datetime.today(), "", "gasto"
    for opt, arg in options:
        if opt in ("-v", "--valor"):
            value = arg
        elif opt in ("-d", "--dia"):
            day = arg
        elif opt in ("-desc", "--descricao"):
            description = arg
        elif opt in ("-t", "--tipo"):
            value_type = arg

    if not value or not str.isdecimal(value):
        raise Exception("O valor deve ser numérico")
    else:
        value = float(value)
    return value, day, description, value_type
