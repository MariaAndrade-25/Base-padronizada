from app.validadores import validar_cpf

def test_cpf_valido():
    assert validar_cpf("52998224725") is True

def test_cpf_invalido():
    assert validar_cpf("12345678900") is False
