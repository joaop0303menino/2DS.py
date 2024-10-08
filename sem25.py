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