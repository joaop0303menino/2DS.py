import random

print('bem vindo ao organizador de torneios')
print('você ira escolher o nome dos participantes com quantidade par, é nos vamos sortear as chaves!\n')

participantes = input(f'digite o nome dos participantes separados por virgula: ').replace(' ','')
participantes_lista = participantes.split(',')

def sorteio(participantes_lista):
  n_chaves = len(participantes_lista) / 2
  c = 1
  while c <= n_chaves:
    participante1 = random.choice(participantes_lista)
    participantes_lista.remove(participante1)
    participante2 = random.choice(participantes_lista)
    participantes_lista.remove(participante2)
    print(f'chave {c}: {participante1} x {participante2}')
    c += 1


if len(participantes_lista) % 2 == 1:
  participantes_lista += [input('digite mais um nome de participante: ')]
  sorteio(participantes_lista)
else:
  sorteio(participantes_lista)