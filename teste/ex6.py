import numpy as np

defeitos_por_caixa = np.array([0, 1, 2, 3, 4, 5])
quantidade_caixas = np.array([20, 12, 19, 10, 4, 1])

mediana = np.median(np.repeat(defeitos_por_caixa, quantidade_caixas))

porcentagem_ate_max_defeitos = np.sum(quantidade_caixas[defeitos_por_caixa <= 2]) / np.sum(quantidade_caixas) * 100

print("Mediana de defeitos por caixa: ", int(mediana))
print("Porcentagem de caixas com no máximo 2 defeitos: ", round(porcentagem_ate_max_defeitos, 2), "%")