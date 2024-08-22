correta = ["p","y","t","h","o","n"]

errada = ["#","#","#","#","#","#"]

def jogo():
    
    for j in range(10):
        
        letter = input("Digite uma letra: ")

        for i in range(len(correta)):
            if letter == correta[i]:
                errada[i] = correta[i]
                
                print(errada)
        
    if errada == correta:
        print(correta)
        print("Parabéns você ganhou o jogo ")
        
    else:
        print("Você só tinha 10 tentativas tente novamente")
        jogo()
            
jogo()
        

