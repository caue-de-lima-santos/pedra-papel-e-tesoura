from random import choice

#apresentação do jogo para o usuário

print("Ola, esse é o famoso jogo de pedra, papel e tesoura!")
print("Funcionara da seguinte forma: você escolhera uma das 3 alternativas e talvez você perca, ganhe ou empate")

#atribuição de variáveis para o usuário e a máquina

options = ["pedra", "papel", "tesoura"]
bot_option = choice(options)
user_option = input("Digite 'pedra', 'papel' ou 'tesoura'").lower()

#cadeias condicionais para exibir o resultado do jogo

if bot_option == user_option:
    print("Deu empate!")
elif (bot_option == "pedra" and user_option == "tesoura") or (bot_option == "tesoura" and user_option == "papel") or (bot_option == "papel" and user_option == "pedra"):
    print("Você perdeu, pois você escolheu {} e a máquina escolheu {}".format(user_option, bot_option))
elif user_option not in options:
    print("Você não digitou 'pedra', 'papel' ou 'tesoura'")
else:
    print("Você ganhou, pois você escolheu {} e a máquina escolheu {}".format(user_option, bot_option))
# feito por caue-de-lima-santos
# 02/06/2024 11:57 PM