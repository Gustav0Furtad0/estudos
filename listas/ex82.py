from random import randint

qtd = int(input("Digite a quantidade de itens a serem inseridos na lista: "))

lista = []  
for i in range(0, qtd):
    #a = int(input(f"Digite o {i+1}° valor para entra na lista: "))
    a = randint(1, 1000)
    lista.append(a)

par = []
impar = []

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"{lista}\n{par}\n{impar}")