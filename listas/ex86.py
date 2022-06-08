ordenada = []

while True:
    if not ordenada:
        print("Lista vazia!!")
        ordenada.append(int(input("Digite um valor para a lista ordenada: ")))
    else:
        n = int(input("Digite um valor para a lista ordenada: "))
        for ix, item in enumerate(ordenada):
            if n < item:
                ordenada.insert(ix, n)
                print("Valor adicionado ordenado sem 'sort'.")
                break
        teste = input("Quer continuar? [SIM/NAO] ")
        if teste.upper()[0] == 'N':
            break

print(ordenada)