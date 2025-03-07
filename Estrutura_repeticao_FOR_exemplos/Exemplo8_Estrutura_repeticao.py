# Pedir 5 números ao usuário e exibi-los


lista = []


for cont in range(5):
    num =  int(input(print("Digite um número: ")))
    lista.append(num)
   
print("Os números digitados foram: ")


for num in lista:
    print(num)
