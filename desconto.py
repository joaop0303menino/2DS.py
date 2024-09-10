def pagar():
    var = float(input("digite o preço: "))
    desconto = int(input("digite o numero do desconto SO O NUMERO SEM %: "))

    var_desconto =  (var*desconto)/100

    pagar = var-var_desconto

    print(f"vc tem um desconto de R$:{var_desconto}")
    print(f"o valor a pagar é {pagar}")

def tempo():
    distancia = int(input("digite a distancia: "))
    velocidade = int(input("digite a velocidade media da rota: "))

    tempo = distancia/velocidade

    print(f" o tempo extimado é de: {tempo}")

def kw():
    kwh = int(input("digite os kwh: "))

    tipo = input("digite o tipo C, R ou I: ").lower()

    if tipo == "r":
        if kwh > 500: 
            print(kwh*0,65)
        else:
            print(kwh*0,40)
    elif tipo == "c":
        if kwh > 1000: 
            print(kwh*0,60)
        else:
            print(kwh*0,55)
    elif tipo == "i":
        if kwh > 5000: 
            print(kwh*0,60)
        else:
            print(kwh*0,55)
    else:
        print("ERRO")
        
        
    