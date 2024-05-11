dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Aqui estamos acessando o valor que está dentro de cada variável!
print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

# Aqui estamos sobrescrevendo o valor das variaveis!
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

# Isso aqui é como vai ficar o dicionário depois da alteração.
print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
