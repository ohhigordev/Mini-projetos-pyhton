def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


#salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Passando os valores de forma sequencial.
#salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Passando o conjunto chave e valor.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Aqui e como se você estivesse passando um dicionario para a função.


