ordenada = []

while True:

    if not ordenada:
        ordenada.append(int(input("Digite um valor para a lista ordenada: ")))
        print(f"Valor adicionado ordenado sem 'sort' na posição {0}.")

    else:
        insere = 0
        n = int(input("Digite um valor para a lista ordenada: "))

        for ix, item in enumerate(ordenada):
            if n < item:
                ordenada.insert(ix, n)
                print(f"Valor adicionado ordenado sem 'sort' na posição {ix}.")
                insere += 1
                break
            
        if insere == 0:
            ordenada.append(n)
            print("O número foi inserido no final da lista ordenada.")

    teste = input("Quer continuar [SIM/NAO]? ")
    if teste.upper()[0] == 'N':
        break

print(ordenada)
