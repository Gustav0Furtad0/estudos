import numpy as np

estaturas = [
    {'estatura': (150 + 154) / 2, 'alunos': 6},
    {'estatura': (154 + 158) / 2, 'alunos': 7},
    {'estatura': (158 + 162) / 2, 'alunos': 10},
    {'estatura': (162 + 166) / 2, 'alunos': 14},
    {'estatura': (166 + 170) / 2, 'alunos': 6},
    {'estatura': (170 + 174) / 2, 'alunos': 11}
]

dados_np = np.array([(d['estatura'], d['alunos']) for d in estaturas], dtype=[('estatura', float), ('alunos', int)])

estatura_media = np.average(dados_np['estatura'], weights=dados_np['alunos'])
print(f'Estatura média: {estatura_media} cm')

abaixo_162 = np.sum(dados_np['alunos'][:3])
porcentagem_162 = (abaixo_162 / np.sum(dados_np['alunos'])) * 100
print(f'Porcentagem de alunos com estatura inferior a 162 cm: {porcentagem_162:.2f}%')

