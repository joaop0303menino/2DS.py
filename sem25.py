estoque = [20,15,10,30,5]


def atualizar(estoque,produto,quantidade):
    if 0 <= produto < len(estoque):
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
        
        else:
            print(f"não a produto suficiente {produto + 1}° ")
            
    else:
        print("PRODUTO INVALIDO ")


def adicionar(estoque,produto,quantidade):
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade
    else:
        print("PRODUTO INVALIDO ")
        
def ver(estoque):
    for i, quantidade in enumerate(estoque):
        print(f"produto: {i + 1}°\n quantidade: {quantidade}")

ver(estoque)



def reserva(assentos,fileira,assento):
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assentos[fileira][assento] == 0:
            assentos[fileira][assento] = 1
            print(f"reservado {fileira + 1}: {assento + 1}")
        else:
            print("ja esta reservado")
    else:
        print("erro")
        
def cancelar(assentos,fileira,assento):
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assentos[fileira][assento] == 1:
            assentos[fileira][assento] = 0
            print(f"reserva cancelada {fileira + 1}: {assento + 1}")
        else:
            print("não esta reservado")
    else:
        print("erro")
        
def ver(assentos):
    for i, fileira in enumerate(estoque):
        print(f"fileira: {i + 1}" + " " .join(str(assento) for assento in fileira))
        
