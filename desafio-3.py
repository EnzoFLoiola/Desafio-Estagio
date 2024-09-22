import json

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

faturamento = []

for dia in dados:
    if dia["valor"] > 0:
        faturamento.append(dia["valor"])


menorFaturamento = min(faturamento)

maiorFaturamento = max(faturamento)

mediaFaturamento = sum(faturamento) / len(faturamento)

diasAcimaMedia = sum(1 for valor in faturamento if valor > mediaFaturamento)

print(f'''O menor valor de faturamento ocorrido em um dia do mês: {menorFaturamento}
O maior valor de faturamento ocorrido em um dia do mês: {maiorFaturamento}
Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {diasAcimaMedia}''')