entrada = input()
lista = [int(x) for x in entrada.split()]
listaOrdenada = sorted(lista)

for v in listaOrdenada:
    print(v)
print()
for v in lista:
    print(v)
