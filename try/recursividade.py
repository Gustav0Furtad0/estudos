from time import sleep

def leint(mensagem):
    a = input(f"{mensagem}")
    while True:
        if a.isnumeric():
            return a
        else:
            print("Erro: Não é um número inteiro")
            a = input(f"{mensagem}")

def leintrecursivo(mensagem):
    a = input(f"{mensagem}")
    if a.isnumeric():
        return a
    else:
        print("Erro: Não é um número inteiro")
        return leintrecursivo(mensagem)

def leintrecursivotry(mensagem):
    try:
        a = int(input(f"{mensagem}"))
    except:
        print("Erro: Não é um número inteiro")
        return leint(mensagem)
    else:
        return a


idade = leintrecursivo("Digite sua idade: ")
sleep(2)
numfav = leintrecursivotry("Digite seu número favorito: ")
sleep(2)
pai = leint("Digite a idaded de seu pai: ")
sleep(2)

print(f'''\nA idade do usuário é {idade}.
Seu número favorito é {numfav}.
\n''')
sleep(2)

print("Fim do programa")