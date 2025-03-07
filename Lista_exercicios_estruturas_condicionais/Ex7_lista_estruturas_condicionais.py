# 7. Ler duas notas de um aluno, efetuar a média aritmética e, se a média for maior ou igual a 7, informar que o aluno foi aprovado; se a média for maior ou igual a 5 mas menor do que 7,
# informar que o aluno está de exame; se a média for menor do que 5 informar que o aluno foi reprovado.


nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))
media = (nota1 + nota2)/2


if media >= 7:
    print ("Você está APROVADO")
if media >= 5 and media < 7:
    print ("Você está de EXAME")
if media < 5:
    print ("Você está REPROVADO")
