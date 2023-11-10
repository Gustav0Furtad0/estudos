import random

cavalos = []

for i in range(1, 25):
    cavalos.append({
            "nome" : f"Cavalo {i}",
            "colocacoes" : [],
            "oponentes_enfrentados" : [],
            "velocidade" : random.randint(1, 30),
        })

for cavalo in cavalos:
    print("Nome:", cavalo["nome"], "Velocidade:", cavalo["velocidade"]);

def corrida(cavalos_para_corrida):
    def insertion_sort_desc(lista):
        for i in range(1, len(lista)):
            atual = lista[i]
            j = i - 1

            while j >= 0 and lista[j]["velocidade"] < atual["velocidade"]:
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = atual

        return lista
    
    cavalos_para_corrida = insertion_sort_desc(cavalos_para_corrida)
    
    for i, cavalo in enumerate(cavalos_para_corrida):
        cavalo["colocacoes"].append(i + 1)
        cavalo["oponentes_enfrentados"].append(cavalos_para_corrida[:i] + cavalos_para_corrida[i + 1:])

    # for cavalo in cavalos_para_corrida:
    #     print("Nome:", cavalo["nome"], "Velocidade:", cavalo["velocidade"], "Colocações:", cavalo["colocacoes"], "Oponentes enfrentados:", cavalo["oponentes_enfrentados"])

corrida([cavalos[0], cavalos[1], cavalos[2], cavalos[3], cavalos[4]])

