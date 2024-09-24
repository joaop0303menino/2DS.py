class Carro:
    def __init__(self, marca, modelo, cor, valor, ano):
        self.marca = marca 
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

class Estoque(Carro):
    def __init__(self):
        self.carros = []
    
    def Adicionar(self, carro):
        self.carros.append(carro)
        
    def Mostrar(self):
        for carro in self.carros:
            print(f"{carro.modelo},{carro.marca}")
        
carro_1 = Carro('BMW','24','azul',2000000,'2013')
carro_2 = Carro('CSS','25','red',4000000,'2023')

estoque = Estoque()

estoque.Adicionar(carro_1)
estoque.Adicionar(carro_2)

estoque.Mostrar()