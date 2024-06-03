from random import choice

#apresentação do jogo para o usuário

print("Ola, esse é o famoso jogo de pedra, papel e tesoura!")
print("Funcionara da seguinte forma: você escolhera uma das 3 alternativas e talvez você perca, ganhe ou empate")

#atribuição de variáveis para o usuário e a máquina

bot_option = choice(["pedra", "papel", "tesoura"])
user_option = input("Digite 'pedra', 'papel' ou 'tesoura'").lower()

#cadeias condicionais para exibir o resultado do jogo

if user_option == bot_option:
    print("Voce e a maquina escolheram {}, logo o resultado foi um empate!".format(user_option))
elif user_option == "pedra" and bot_option == "papel":
    print("A maquina escolheu {}, e voce escolheu {}, logo a máquina venceu!".format(bot_option, user_option))
elif user_option == "pedra" and bot_option == "tesoura":
    print("A maquina escolheu {}, e voce escolheu {}, logo você venceu!".format(bot_option, user_option))
elif user_option == "tesoura" and bot_option == "pedra":
    print("A maquina escolheu {}, e voce escolheu {}, logo a máquina venceu!".format(bot_option, user_option))
elif user_option == "tesoura" and bot_option == "papel":
    print("A maquina escolheu {}, e voce escolheu {}, logo você venceu!".format(bot_option, user_option))
elif user_option == "papel" and bot_option == "tesoura":
    print("A maquina escolheu {}, e voce escolheu {}, logo a máquina venceu!".format(bot_option, user_option))
elif user_option == "papel" and bot_option == "pedra":
    print("A maquina escolheu {}, e voce escolheu {}, logo você venceu!".format(bot_option, user_option))
else:
    print("Não foi possivel realizar o jogo, pois voce digitou algo que não corresponde com 'pedra','papel' ou 'tesoura'")

# feito por caue-de-lima-santos
# 02/06/2024 11:57 PM