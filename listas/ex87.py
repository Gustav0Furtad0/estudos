from operator import indexOf


numeros = []

while True:
    numeros.append(int(input("Digite um núemro: ")))
    teste = input("Quer continuar [SIM/NAO]? ")
    if teste.upper()[0] == 'N':
        break
print(f"Aquantidade de números digitados é {len(numeros)}.")

numeros.sort(reverse=True)

print(f"A lista ordenada de forma decrescente é {numeros}")

if 5 in numeros:
    print(f"O número 5 está na lista na posição {numeros.index(5)}")
else:
    print("O número 5 não esá na lista")