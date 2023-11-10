def verificar_tipo_triangulo(a, b, c):
    if a == b == c:
        return 'equilatero'
    elif a == b or a == c or b == c:
        return 'isosceles'
    else:
        return 'escaleno'

def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if verificar_triangulo(A, B, C):
    print("É um triangulo", verificar_tipo_triangulo(A, B, C))
else:
    print("Os lados não formam um triangulo!")
