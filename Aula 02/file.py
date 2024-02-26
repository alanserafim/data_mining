# ================>  Variáveis

nome = 'Alan'
idade = 32
peso = 75.55


# ================> Impressão no terminal 

print(f"Menu nome é {nome} e minha idade é {idade} anos")

# =================> Operações matemáticas
soma = idade + 5
subtracao = idade - 2   
multiplicacao = idade * 3
divisao = idade / 5

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


# =================> strings
frase = "Nome: " + nome + ", idade: " + str(idade) + "."
print(f'Frase: {frase}')


# =================> Relacionais
teste_idade = idade >= 18
teste_nome = nome == "Alan"

print(f"Idade: {teste_idade}")
print(f"Nome: {teste_nome}")

# ==================> Funções
tamanho_nome = len(nome)

print(f"Quantidade de caracteres do nome: {tamanho_nome}")

## =================> Laços
print("\nfor in loop")
for i in range(5):
    print(f"index: {i}")


print("\nwhile loop")
numero = 1
while numero<= 5:
    print(f"numero: {numero}")
    numero += 1