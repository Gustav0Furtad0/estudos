from time import sleep
from random import randint

qtd = int(input("Digite a quantidade de itens a serem inseridos na lista: "))

lista = []
for i in range(0, qtd):
    #a = int(input(f"Digite o {i+1}° valor para entra na lista: "))
    a = randint(1, 1000)
    lista.append(a)

print("Foram incrementados os itens na lista!")
print(f"Atualmente a lista tem {len(lista)} itens.")
sleep(1.5)
print("-" * 60, end="\n\n")
print(f'{"Verificando maior e menor valores...":^40}', end="\n\n")
print("-" * 60, end="\n\n")
sleep(3)

menor = [lista[0], 0]
maior = [lista[0], 0]

for pos, item in enumerate(lista):
    if maior[0] < item:
        maior[0] = item
        maior[1] = pos
    if menor[0] > item:
        menor[0] = item
        menor[1] = pos

print(f'''O maior valor da lista é {maior[0]} na posição {maior[1]}.
Já o menor é {menor[0]} na posição {menor[1]}.''')
print(f"Portanto o maior intervelo entre os número das lista é {maior[0]-menor[0]}")
print(lista)
print("\n\n")
