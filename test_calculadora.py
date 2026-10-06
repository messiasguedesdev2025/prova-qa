from calculadora import calcular_desconto


# Compras COMUM

def test_compra_abaixo_de_100():
    assert calcular_desconto(99, "COMUM") == 0


def test_compra_exatamente_100():
    assert calcular_desconto(100, "COMUM") == 10


def test_compra_entre_100_e_500():
    assert calcular_desconto(300, "COMUM") == 30


def test_compra_exatamente_500():
    assert calcular_desconto(500, "COMUM") == 100


def test_compra_acima_de_500():
    assert calcular_desconto(1000, "COMUM") == 200


def test_compra_muito_baixa():
    assert calcular_desconto(50, "COMUM") == 0


# Clientes VIP

def test_vip_abaixo_de_100():
    assert calcular_desconto(50, "VIP") == 2.50


def test_vip_exatamente_100():
    assert calcular_desconto(100, "VIP") == 15


def test_vip_entre_100_e_500():
    assert calcular_desconto(300, "VIP") == 45


def test_vip_exatamente_500():
    assert calcular_desconto(500, "VIP") == 125


def test_vip_acima_de_500():
    assert calcular_desconto(1000, "VIP") == 200


# VIP com diferentes letras

def test_vip_minusculo():
    assert calcular_desconto(300, "vip") == 45


def test_vip_misto():
    assert calcular_desconto(300, "Vip") == 45


def test_vip_maiusculo_misto():
    assert calcular_desconto(300, "vIp") == 45


# Regra do teto

def test_teto_de_200_reais():
    assert calcular_desconto(2000, "COMUM") == 200


def test_teto_de_200_reais_para_vip():
    assert calcular_desconto(2000, "VIP") == 200


def test_teto_para_compra_de_1500():
    assert calcular_desconto(1500, "COMUM") == 200


def test_teto_para_vip_1500():
    assert calcular_desconto(1500, "VIP") == 200
