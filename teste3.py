import json


with open("dados.json", encoding='utf-8') as dados_fornecidos:
    dados = json.load(dados_fornecidos)

valor = []
dados_sem_zeros = []

for dado in dados:
    if dado['valor'] != 0:
        valor.append(dado['valor'])
        dados_sem_zeros.append(dado)

media_faturamento_mensal = sum(valor)/len(valor)
media_faturamento_mensal

valor_maximo = max(dados, key=lambda x:x['valor'])
valor_minimo = min(dados_sem_zeros, key=lambda x:x['valor'])

dias_acima_media = 0
for dado in dados:
    if dado['valor'] > media_faturamento_mensal:
        dias_acima_media += 1
        
print("")
print(f"O menor valor de faturamento ocorrido em um dia do mês é de {valor_minimo['valor']} no dia {valor_minimo['dia']}")
print(f"O maior valor de faturamento ocorrido em um dia do mês é de {valor_maximo['valor']} no dia {valor_maximo['dia']}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é igual a {dias_acima_media}")
print("")