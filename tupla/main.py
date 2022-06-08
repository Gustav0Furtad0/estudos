produtos = ("tenis de mesa", "arredar", "trem", "mucadique")
vogais = "A", "E", "I", "O", "U"

for produto in produtos:
    print(f"A palavra '{produto}' tem as vogais ", end="")
    for vogal in vogais:
        if(vogal in produto.upper()):
            print(vogal, end=" ")
    print("\n")
    