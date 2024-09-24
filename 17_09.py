

numeros = []

for i in range(3):
    numero = int(input("digite um numero: "))
    numeros.append(numero)

print(f"o maior numero é {max(numeros)} e o menor é {min(numeros)}")

#60d 0.15km

dias = int(input("quantos dias você ficou com a carro: "))
km = float(input("quantos KM você rodou com o carro: "))

print(f"você andou {km}KM e ficou {dias} dias com o carro e gastou: R$:{(km*0.15)+(dias*60)}")