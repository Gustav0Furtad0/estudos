from configparser import LegacyInterpolation


expre = str(input("Digite uma expressão: "))

para = [0, 0]

for i in range(0, len(expre)):
    if expre[i] == '(':
        para[0] += 1
    elif expre[i] == ')':
        para[1] += 1
    else:
        pass

if para[0] == para[1]:
    print("Sua expressão é válida")
else:
    print("Expressão inválida")
