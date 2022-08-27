import random

pedra = '''
    _______
---' ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---' ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---' ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Escreva seu código abaixo desta linha 👇

game_imagens = [pedra, papel, tesoura]

escolha_usuario = int(input(
    "O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
if escolha_usuario >= 3 or escolha_usuario < 0:
    print("Você digitou um número inválido, você perde!")
else:
    print(game_imagens[escolha_usuario])

    escolha_computador = random.randint(0, 2)
    print("O computador escolheu:")
    print(game_imagens[escolha_computador])

    if escolha_usuario == 0 and escolha_computador == 2:
        print("Você ganhou!")
    elif escolha_computador == 0 and escolha_usuario == 2:
        print("Você perdeu")
    elif escolha_computador > escolha_usuario:
        print("Você perdeu")
    elif escolha_usuario > escolha_computador:
        print("Você ganhou!")
    elif escolha_computador == escolha_usuario:
        print("Está empatado")
# aleatorio_inteiro = random.randint(1, 10)
# print(aleatorio_inteiro)

# aleatorio_flutuante = random.random()
# soma = aleatorio_flutuante * 5
# print(soma)
