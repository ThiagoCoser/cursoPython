# Todos os programas Python podem chamar um conjunto básico de funções chamadas funções integradas,
# incluindo as funções print(), input() e len() que você viu antes.
# Python também vem com um conjunto de módulos denominado biblioteca padrão.
# Cada módulo é um programa Python que contém um grupo relacionado de funções que podem ser incorporado
# em seus programas. Por exemplo, o módulo matemático (math) possui um conjunto de funções matemáticas,
# o módulo aleatório (random) tem funções relacionadas a números aleatórios, o módulo (time) possui funções de tempo,
# o módulo de teclado (keyboard) permite utilizar as teclas do teclado e assim por diante.


# Antes de poder usar as funções em um módulo, você deve importar o arquivo módulo com uma instrução de importação. No código,
# uma instrução de importação consiste em:

# • A palavra-chave de importação (import)
# • O nome do módulo (exemplo, import time)
# • Opcionalmente, mais nomes de módulos, desde que separados por vírgulas

# Depois de importar um módulo, você pode usar todas as funções interessantes desse módulo.
#  Vamos tentar com o módulo aleatório, que nos dará acesso a função random.ranint()


#%%
# Sorteia um número aleatório usando a função random.ranint() do módulo random
import random

numeroAleatorio = random.randint(1, 10)
print(numeroAleatorio)

#%%
import time

tempo = 10

while (tempo>0):
    tempo-=1
    print(tempo)
    time.sleep(1)

print ("Terminou")


#%%
#Isto cria seu próprio módulo, importando uma função customizada
# a partir de outro script
#ScriptA

def somaNumeros(num1, num2):
  return num1+ num2

a = 5
b = 3

c= somaNumeros(a,b)

print(c)

#ScriptB
#import ScriptA

a = 10
b = 12

# Importa a função modular da biblioteca do ScriptA
# c = ScriptA.somaNumeros(a,b)
print(c)

# %%
