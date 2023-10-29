# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre
# Calcule a sua média. A atribuição de conceitos obedece à tabela:

# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 - A
# Entre 7.5 e 9.0 - B
# Entre 6.0 e 7.5 - C
# Entre 4.0 e 6.0 - D
# Entre 4.0 e zero - E

n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
m = (n1 + n2) / 2
print("A média é igual a {}".format(m))

if m==0 and m<=4:
    print("Você tirou E, precisa estudar mais")
if m>=4.1 and m<=6:
    print("Você tirou D, precisa estudar mais")
if m>=6.1 and m<=7.5:
    print("Você tirou C, tá quase lá")
if m>=7.6 and m<=8.9:
    print("Você tirou B, parabéns!")
if m==9 and m==10:
    print("Você tirou A, parabéns!!")
    
# if é usada para testar se a condição é verdadeira ou falsa. Se for verdadeira, o código dentro do "if" é executado, caso contrário é ignorado.
# and é usado para combinar duas condições. ele retorna "true" somente se as duas condições forem verdadeiras.
