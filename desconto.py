var = float(input("digite o preço: "))
desconto = int(input("digite o numero do desconto SO O NUMERO SEM %: "))

var_desconto =  (var*desconto)/100

pagar = var-var_desconto

print(f"vc tem um desconto de R$:{var_desconto}")
print(f"o valor a pagar é {pagar}")