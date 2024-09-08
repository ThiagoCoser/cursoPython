#%%
# Formatação de Strings

# F-String foi introduzido no Python 3.6 e agora é a forma
# preferida de formatar strings.

# Antes do Python 3.6, tínhamos que usar o método format().

# Permite formatar partes selecionadas de uma string.

# Para especificar uma string como uma string f, basta colocar
# um f na frente da string literal, assim:

txt = f"Olá mundo!"
print(txt)

#%%

# Placeholders
# Para formatar valores em uma string f, adicione espaços reservados {}.
# Um espaço reservado pode conter variáveis,
# operações, funções e modificadores para formatar o valor.

preço = 100
txt = f"O preço é R#{preço},00"
print(txt)

# %%
# Modificadores
# Um espaço reservado também pode incluir um modificador
#  para formatar o valor.

# Um modificador é incluído adicionando dois pontos : seguido
#  por um tipo de formatação, como .2f que significa número
#  de ponto fixo com 2 casas decimais:

preço = 100
txt = f"O preço é de {preço:.2f} reais"
print(txt)


# %%

#Podemos colocar uma variável diretamente

info = f"Este número {95.513:.2f} foi formatado"
print(info)


# %%

#Ou operacionalizar valores

txt = f"O preço mais a quantidade deu {100 * 5} reais"
print(txt)
# %%

# Você pode executar instruções if...else dentro dos espaços reservados:

preço= 100
txt = f"É muito {'Caro' if preço>100 else 'Barato'}"

print(txt)
# %%
