from utils import extract_arguments

def test_extract_arguments():
    expected = [['-v', '11'], ['-t', 'Comprasmercadinho'], ['-h', '']]
    
    _input = ('/newfin -v 11 -t Compras mercadinho -h',)
    
    result = extract_arguments(_input)

    assert result == expected