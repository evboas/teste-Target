faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

percentuais = []
for valor in faturamento.values():
    percentuais.append((valor/total)*100)

estados = []
for estado in faturamento:
    estados.append(estado)

lista_estado_percentual_faturamento = {}
numero_estados = len(estados)
for i in range(numero_estados):
    lista_estado_percentual_faturamento[estados[i]] = percentuais[i]
    print(f'{estados[i]} = {round(percentuais[i],3)}%')