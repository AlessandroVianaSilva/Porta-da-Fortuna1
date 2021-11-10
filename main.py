from random import randint #biblioteca random - função randint

print('''
                Porta da Fortuna
++++++++++++++++++++++++++++++++++++++++++++++++++
  Acerte o numero premiado que atrás de uma porta!
  Advinhe qual é a porta certa para ganhar!
                     _______  
                    |       |
                    |  [?]  |
                    |       |  
                     -------        
''')

nome = input("Digite seu Nome: ") #nome do jogador

print('Quer tentar em qual nível de dificuldade?')
print('(1) Fácil  (2) Médio  (3) Difícil')
nivel = int(input("Defina seu nível: "))

if(nivel == 1): #se colocar 1 
    total_tentativas = 3
    porta_certa = randint(1,5)
    print('Acerte um numero entre 1 e 5')
elif(nivel == 2):
    total_tentativas = 3 #se colocar 2
    porta_certa = randint(1,8)
    print('Acerte um numero entre 1 e 8')
else:
    total_tentativas = 3 #se colocar 3
    porta_certa = randint(1,10)
    print('Acerte um numero entre 1 e 10')

for tentativa in range(1,total_tentativas + 1): 
    print('Tentativa ', tentativa,' de ',total_tentativas)
    chute_jogador = int(input('Digite um número: ')) #a tentativa no momento e total de tentativas que o jogador tem para acertar
    acertou = chute_jogador == porta_certa
    maior   = chute_jogador > porta_certa
    menor   = chute_jogador < porta_certa #variaveis

    if(acertou): #se acertar
        print('Parabéns! Você acertou')
        print("A porta certa está no numero: ",porta_certa)
        break #interrompe o codigo se estiver correto
    elif tentativa >= 3:
      print(" Voce perdeu!")
      print("a porta certa estava no numero: " ,porta_certa)
    else:
      if(menor):
         print('Lamento, você errou! Seu chute foi menor que o número da porta certa')
      elif(maior):
        print('Lamento, você errou! Seu chute foi maior que o número da porta certa')


print('FIM DO JOGO')
