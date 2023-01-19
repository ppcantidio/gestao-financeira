from src.rules.extrato import Extrato
from datetime import datetime

mocker_despesa_recorrente = "src.rules.extrato.DespesaRecorrente"
mocker_receita_recorrente = "src.rules.extrato.ReceitaRecorrente"


lista_despesas_recorrentes = [
    {"nome": "Parcela carro", "valor": 760, "categoria": "Financeiamentos", "dt_pagamento": datetime.now()},
    {"nome": "Seguro carro", "valor": 400, "categoria": "Seguros", "dt_pagamento": datetime.now()},
]
lista_receitas_recorrentes = [
    {"nome": "Salario", "valor": 4600, "categoria": "Trabalho", "dt_pagamento": datetime.now()},
    {"nome": "Freelancer", "valor": 400, "categoria": "Trabalho", "dt_pagamento": datetime.now()},
]


def test_retorna_extrato(mocker):
    mocker.patch(f"{mocker_despesa_recorrente}.retorna_despesas_recorrentes", return_value=lista_despesas_recorrentes)
    mocker.patch(f"{mocker_receita_recorrente}.retorna_receitas_recorrentes", return_value=lista_receitas_recorrentes)
    extrato = Extrato("63921a42555d44aa0cb2b6af").gerar_extato("012023")
    print(extrato)
