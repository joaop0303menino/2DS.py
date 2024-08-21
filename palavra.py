correta = ["p","y","t","h","o","n"]

errada = ["#","#","#","#","#","#"]

letter_correct = []

def jogo():
    
    for j in range(10):
        
        letter = input("Digite uma letra: ")

        for i in range(len(correta)):
            if letter == correta[i]:
                print(letter_correct)
                letter_correct.append(letter)
            else:
                print(errada[i])
        
    if letter_correct == correta:
        print(correta)
        print("Parabéns você ganhou o jogo ")
        
    else:
        print("Você só tinha 10 tentativas tente novamente")
        jogo()
            
jogo()
        

