# 12. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.




dia_da_semana = int(input("Digite um numero de 1 a 7 para descobrir o dia da semana: "))


match (dia_da_semana):


      case 1:
        print("Domingo")
      case 2:
        print("Segunda-feira")
      case 3:
        print("Terça-feira")
      case 4:
        print("Quarta-feira")
      case 5:
        print("Quinta-feira")
      case 6:
        print("Sexta-feira")
      case 7:
        print("Sabado")
      case _:
        print("Valor Inválido!")