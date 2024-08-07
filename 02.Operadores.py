# Operadores Aritméticos
print("Operadores Aritméticos")
a = 5
b = 3
print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão Inteira: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Exponenciação: {a} ** {b} = {a ** b}\n")

# Operadores de Comparação
print("Operadores de Comparação")
a = 5
b = 3
print(f"Igual a: {a} == {b} -> {a == b}")
print(f"Diferente de: {a} != {b} -> {a != b}")
print(f"Maior que: {a} > {b} -> {a > b}")
print(f"Menor que: {a} < {b} -> {a < b}")
print(f"Maior ou igual a: {a} >= {b} -> {a >= b}")
print(f"Menor ou igual a: {a} <= {b} -> {a <= b}\n")

# Operadores Lógicos
print("Operadores Lógicos")
a = True
b = False
print(f"E lógico: {a} and {b} -> {a and b}")
print(f"Ou lógico: {a} or {b} -> {a or b}")
print(f"Não lógico: not {a} -> {not a}\n")

# Operadores de Atribuição
print("Operadores de Atribuição")
a = 5
print(f"Atribuição: a = {a}")
a += 3
print(f"Atribuição com adição: a += 3 -> {a}")
a -= 3
print(f"Atribuição com subtração: a -= 3 -> {a}")
a *= 3
print(f"Atribuição com multiplicação: a *= 3 -> {a}")
a /= 2
print(f"Atribuição com divisão: a /= 2 -> {a}\n")

# Operadores de Identidade
print("Operadores de Identidade")
a = [1, 2, 3]
b = a
print(f"É: a is b -> {a is b}")
c = [1, 2, 3]
print(f"Não é: a is not c -> {a is not c}\n")

# Operadores de Associação
print("Operadores de Associação")
a = [1, 2, 3]
print(f"Em: 2 in a -> {2 in a}")
print(f"Não em: 4 not in a -> {4 not in a}\n")

# Operadores Bitwise
print("Operadores Bitwise")
a = 5  # 0101 em binário
b = 3  # 0011 em binário
print(f"E bitwise: {a} & {b} -> {a & b}")  # 0001 em binário
print(f"Ou bitwise: {a} | {b} -> {a | b}")  # 0111 em binário
print(f"Xor bitwise: {a} ^ {b} -> {a ^ b}")  # 0110 em binário
print(f"Negação bitwise: ~{a} -> {~a}")  # invertendo todos os bits de 5
print(f"Deslocamento à esquerda: {a} << 1 -> {a << 1}")  # 1010 em binário
print(f"Deslocamento à direita: {a} >> 1 -> {a >> 1}")  # 0010 em binário
