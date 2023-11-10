import random
from itertools import combinations

def identificar_3_cavalos_mais_rapidos(cavalos):
    nomes_cavalos = list(cavalos.keys())

    # Gera todas as combinações únicas de pares de cavalos
    combinacoes = list(combinations(nomes_cavalos, 2))

    # Realiza as primeiras 15 corridas
    resultados_corridas = {}
    for i in range(3):  # 3 rodadas de 5 corridas cada
        corridas = realizador_corridas_unicas(combinacoes, 5)
        resultados_corridas[f"Rodada_{i+1}"] = corridas

    # Elimina os 10 cavalos de menor média após as primeiras 15 corridas
    cavalos_restantes = list(cavalos.keys())
    for rodada, corridas in resultados_corridas.items():
        cavalos_restantes = eliminar_cavalos_menor_media(corridas, cavalos_restantes)

    # Realiza as corridas restantes
    for i in range(3, 5):  # 2 rodadas de 5 corridas cada
        corridas = realizador_corridas_unicas(combinacoes, 5)
        resultados_corridas[f"Rodada_{i+1}"] = corridas

    # Ordena os cavalos restantes com base na última rodada
    cavalos_ordenados = ordenar_cavalos(resultados_corridas[f"Rodada_{i+1}"], cavalos_restantes)

    # Retorna os 3 cavalos mais rápidos
    return cavalos_ordenados[:3]

def realizador_corridas_unicas(combinacoes, num_cavalos_corrida):
    # Embaralha a ordem das combinações
    random.shuffle(combinacoes)
    # Divide as combinações em grupos de num_cavalos_corrida
    grupos = [combinacoes[i:i+num_cavalos_corrida] for i in range(0, len(combinacoes), num_cavalos_corrida)]
    # Realiza as corridas e obtém os tempos
    tempos_corrida = {cavalo: random.randint(1, 100) for grupo in grupos for corrida in grupo for cavalo in corrida}
    return tempos_corrida

def eliminar_cavalos_menor_media(corridas, cavalos):
    # Calcula a média de colocação apenas para os cavalos presentes nas corridas
    medias = {cavalo: sum(corridas[cavalo]) / len(corridas.get(cavalo, [])) for cavalo in cavalos}

    # Ordena os cavalos com base nas médias e elimina os 10 com menor média
    cavalos_ordenados = sorted(cavalos, key=lambda cavalo: medias[cavalo])
    return cavalos_ordenados[10:]

def ordenar_cavalos(corridas, cavalos):
    # Ordena os cavalos com base nos tempos da última corrida
    cavalos_ordenados = sorted(cavalos, key=lambda cavalo: corridas[cavalo])
    return cavalos_ordenados

# Exemplo de uso
cavalos = {'Cavalo1': 0, 'Cavalo2': 0, 'Cavalo3': 0, 'Cavalo4': 0, 'Cavalo5': 0, 'Cavalo6': 0, 'Cavalo7': 0, 'Cavalo8': 0, 'Cavalo9': 0, 'Cavalo10': 0, 'Cavalo11': 0, 'Cavalo12': 0, 'Cavalo13': 0, 'Cavalo14': 0, 'Cavalo15': 0, 'Cavalo16': 0, 'Cavalo17': 0, 'Cavalo18': 0, 'Cavalo19': 0, 'Cavalo20': 0, 'Cavalo21': 0, 'Cavalo22': 0, 'Cavalo23': 0, 'Cavalo24': 0, 'Cavalo25': 0}
cavalos_mais_rapidos = identificar_3_cavalos_mais_rapidos(cavalos)

print("Os 3 cavalos mais rápidos são:", cavalos_mais_rapidos)
