import argparse
from datetime import datetime

parser = argparse.ArgumentParser(prog='PersonalFinance')

parser.add_argument('-desc', '--description', action='store')
parser.add_argument('-d', '--dia', action='store',
                    type=lambda s: datetime.strptime(s, '%d-%m-%Y'))
parser.add_argument('-t', '--tipo', action='store',
                    choices=['gasto variavel', 'gasto fixo', 'receita'])
parser.add_argument('-v', '--valor', action='store', type=float, default=0)

print(parser.parse_args())
