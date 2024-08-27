joao = [300, 500, 200, 800]
pedro = [200, 400, 500, 700]

def usando_sum(var1, var2):
    mes_joao = sum(var1)
    mes_pedro = sum(var2)

    if mes_joao == mes_pedro:
        print("Os dois gastaram a mesma quantidade")
        
    elif mes_pedro > mes_joao:
        print("O Pedro gastou mais")

    else:
        print("O João gastou mais")
    
usando_sum(joao, pedro)

palavras = ['python','hello word','for','oi']

maxi = max(palavras, key=len)
mini = min(palavras, key=len)
print(f"A maior palavra é {maxi} e a menor é {mini}")
    




        
   



    
    