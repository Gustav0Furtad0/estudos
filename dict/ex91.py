from random import randint

jogadores = dict()
jogador = dict()
for i in range(1,5):
    nome = str(input(f"Digite o nome do jogador {i}: "))
    jogada = randint(1, 6)
    jogadores.update({
        f"jogador{i}": {
            "nome": nome,
            "jogada": jogada
        }
    })
    print(f"Sua jogada foi {jogada}")

print(jogadores)
