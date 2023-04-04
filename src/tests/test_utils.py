from utils import extract_arguments


def test_extract_arguments():
    expected = [['-v', '11'], ['-t', 'Compras mercadinho'], ['-h', '']]
    _input = ('/newfin -v 11 -t Compras mercadinho -h',)
    
    result = extract_arguments(_input)
    assert result == expected


def test_extract_arguments_with_more_args():
    expected = [['-v', '11'], ['-dc', 'Compras mercadinho da silva'], ['-h', '']]
    _input = ('/newfin -v 11 -dc Compras mercadinho da silva -h',)
    
    result = extract_arguments(_input)
    assert result == expected