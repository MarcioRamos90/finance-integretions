# ('/newfin -v 11 -t Compras mercadinho -h',)
from collections import defaultdict

def extract_arguments(args: tuple[str]):
    data = args[0].split()[1:]
    print(data)
    accumulator = []
    
    for i in data:
        if i.startswith("-"):
            accumulator.append([i, ""])
        elif len(accumulator) > 0:
            accumulator[-1][1] += i
    
    return accumulator
