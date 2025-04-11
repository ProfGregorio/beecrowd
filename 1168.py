controle = [6,2,5,5,4,5,6,3,7,6]
leds_controle = []

N = int(input())
i = 0

while i < N:
    vari = input()
    leds = 0
    for valor in vari:
        leds += controle[int(valor)]
    leds_controle.append(leds)
    i += 1

for led in leds_controle:
    print(f"{led} leds")
