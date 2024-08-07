#####1
print ("Olá mundo!")

##### 2
dia=5
mês=7
ano=2024
print ("Campinas",dia, "/", mês, "/", ano)


#####3
a=5
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)


#####4
nome =input("Digite seu nome")
idade = input("Digite sua idade")
peso = input("Digite seu peso")

print("Olá", nome, "! Sua idade é",idade,"e seu peso é", peso)


######5

# Solicita o valor em metros ao usuário
valor = input("Digite o valor em metros: ")

# Converte o valor para float
valor = float(valor)

# Converte metros para milímetros
valorFinal = valor * 1000

# Exibe o valor em milímetros
print(f"Valor em milímetros: {valorFinal}")


#####6

# Solicita a temperatura em Celsius ao usuário
valor = input("Digite a temperatura em Celsius: ")

# Converte o valor para float
valor = float(valor)

# Converte Celsius para Fahrenheit
valorFinal = (valor * 9 / 5) + 32

# Exibe o valor em Fahrenheit
print("O valor em Fahrenheit é", valorFinal)


######7

salarioAtual = input("Digite seu salário atual: ")
aumento = input("Digite o valor do aumento em % ")

salarioAtual = float(salarioAtual)
aumento = float(aumento)

novoSalario = salarioAtual + salarioAtual * aumento / 100
ganhoAnualAumentado = salarioAtual * aumento / 100 * 12

# Exibir resultados, em f-string (formatted string literal)
print(f"Seu salário atual é R${novoSalario:.2f}")
print(f"Seu ganho anual aumentou em R${ganhoAnualAumentado:.2f}")


#####8

# Solicite as notas
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

# Média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificar aprovação
if media >= 7:
    resultado = "aprovado :)"
else:
    resultado = "reprovado :("

# Exibe a média e o resultado
print(f"A média do aluno é: {media:.2f}")
print(f"O aluno foi {resultado}.")

######9
a=5
b=3

resultado = round(a/b,1)
print(resultado)
#print(f"{round(a / b, 3)}")s


######10

print ("“Terminei, estou adorando programar”!")

######11

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
