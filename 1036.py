from math import sqrt

entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = B**2 - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    raiz = sqrt(delta)
    R1 = (-B + raiz) / (2 * A)
    R2 = (-B - raiz) / (2 * A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
