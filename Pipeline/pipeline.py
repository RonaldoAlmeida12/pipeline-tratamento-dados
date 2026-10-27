from copy import deepcopy
from decimal import Decimal, InvalidOperation

registros = [
    {"id": 1, "valor": "120", "status": " Aprovada "},
    {"id": 2, "valor": "inválido", "status": "aprovada"},
    {"id": 3, "valor": "80", "status": "APROVADA"},
    {"id": 4, "valor": "-30", "status": "aprovada"},
    {"id": 5, "valor": 200, "status": "cancelada"},
    {"id": 6, "valor": "50", "status": "aprovada"},
    {"id": 7, "valor": None, "status": "aprovada"},
    {"id": 8, "valor": "90.5", "status": "aprovada"},
    {"id": 9, "valor": "0", "status": "aprovada"},
    {"id": 10, "valor": "250.75", "status": " aprovada "},
    {"id": 11, "valor": "45", "status": "pendente"},
    {"id": 12, "valor": True, "status": "aprovada"},
    {"id": 13, "valor": "300", "status": "aprovada"},
    {"id": 14, "valor": "-12.50", "status": "aprovada"},
    {"id": 15, "valor": "75.25", "status": "APROVADA"},
    {"id": 16, "valor": "abc123", "status": "aprovada"},
    {"id": 17, "valor": 60, "status": "aprovada"},
    {"id": 18, "valor": "180", "status": "cancelada"},
    {"id": 19, "valor": "0.01", "status": "aprovada"},
    {"id": 20, "valor": False, "status": "aprovada"}
]


def relatorio_final(vendas, quantidade, qtde_reprovados):
    return f'Vendas aprovadas: R${vendas:.2f}\n' f'Aprovados: {quantidade}\n' f'Reprovados: {qtde_reprovados}'

def acumulador_vendas(registro, vendas, quantidade, reprovados):
    if registro['valor'] > 0:
        vendas += registro['valor']
        quantidade += 1
    elif registro['valor'] <= 0:
        quarentena(registro, reprovados)
    return vendas, quantidade
   
def quarentena(valor, reprovados):
    reprovados.append(valor)
    
def pipeline_trata_dados(lista):
    vendas = 0
    quantidade = 0
    reprovados = []
    conjunto = {'aprovada', 'cancelada'}
    tratamento = list(deepcopy(lista))
    for registro in tratamento:
        status = registro['status'].strip().lower()
        registro['status'] = status
        if registro['valor'] is None or registro['status'] == 'cancelada':
             quarentena(registro, reprovados)
             continue
        elif registro['status'] not in conjunto:
            quarentena(registro, reprovados)
            continue
        elif isinstance(registro['valor'], bool):
            quarentena(registro, reprovados)
            continue
        try:
            if isinstance(registro['valor'], str) or isinstance(registro['valor'], int):
                registro['valor'] = Decimal(registro['valor'])
        except (InvalidOperation, TypeError):
            quarentena(registro, reprovados)
            continue
        if registro['status'] == 'aprovada':
            vendas, quantidade = acumulador_vendas(registro, vendas, quantidade, reprovados)
    qtde_reprovados = len(reprovados)
    final = relatorio_final(vendas, quantidade, qtde_reprovados)
    return final, reprovados

relatorio, reprovado = pipeline_trata_dados(registros)

print(relatorio)
