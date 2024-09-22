faturamentoEstados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamentoTotal = sum(faturamentoEstados.values())

percentuais = {}

for estado, valor in faturamentoEstados.items():
    percentual = (valor / faturamentoTotal) * 100
    percentuais[estado] = percentual

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")