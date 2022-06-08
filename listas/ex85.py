from time import sleep

numeros = []

while True:
    numif = int(input("Digite um número: "))
    if numif in numeros:
        print("Esse número já existe na lista!!")
    else:
        numeros.append(numif)
        teste = input("Quer continuar? [SIM/NAO] ")
        if teste.upper()[0] == 'N':
            break

numeros.sort()
print(numeros)

sleep(2)