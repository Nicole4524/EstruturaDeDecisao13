#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

diaint = int(input("Digite o valor entre 1 e 7correspondente a um dia da semana: "))

if diaint == 1:
    print("Domingo")

elif diaint == 2:
    print("Segunda-Feira")

elif diaint == 3:
    print("Terça-Feira")

elif diaint == 4:
    print("Quarta-Feira")

elif diaint == 5:
    print("Quinta-Feira")

elif diaint == 6:
    print("Sexta-Feira")

elif diaint == 7:
    print("Sábado")

else:
    print("Valor inválido")
