numeros = []

while True:
    numeros.append(int(input("Digite um núemro: ")))
    teste = input("Quer continuar? [SIM/NAO] ")
    if teste.upper()[0] == 'N':
        break

numeros.sort()
print(numeros)
