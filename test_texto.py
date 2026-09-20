from minha_biblioteca import contar_palavras, inverter_texto

def test_contar_palavras():
    assert contar_palavras("Python é muito legal") == 4

def test_inverter_texto():
    assert inverter_texto("Python") == "nohtyP"
