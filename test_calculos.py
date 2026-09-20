from minha_biblioteca import soma, subtracao, multiplicacao, media

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(5, 2) == 3

def test_multiplicacao():
    assert multiplicacao(4, 3) == 12

def test_media():
    assert media(10, 20, 30) == 20
