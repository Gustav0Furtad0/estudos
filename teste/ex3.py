def insertion_sort(lista):
    # Percorre o vetor
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        # Verifica os elementos anteriores ao "atual" e troca caso seja maior até não seja mais
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
    
        # Insere o valor na posição correta (último valor maior que o "atual")
        lista[j + 1] = atual

    return lista

LISTA = [5, 3, 2, 4, 7, 1, 0, 6]
print(insertion_sort(LISTA))