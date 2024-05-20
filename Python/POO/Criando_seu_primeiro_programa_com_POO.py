
# Criando a classe chamada bicicletas:
class bicicleta:
    # Vamos colocar o nosso construtor ou inicializador:
    def __init__(self, cor, modelo, ano, valor):
        # self é a referência explicita do objeto que foi passado:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    # Definindo metodos de comportamento da nossas bicicletas:
    def buzinar(self):
        print('Piiiiii')

    def parar(self):
        print('Parando a bicicleta')
        print('Bicicleta parada')

    def correr(self):
        print('Vrummmmmmmm')
    
    # Como exibir a nossa instância e fazer uma representação mais legivel:
    #def __str__(self):
       # return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={'R$', self.valor}"
    
    # Como deixar a instancia mais automatizada:
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"



# Definindo os modelos de bicicleta da nossa loja:
b1 = bicicleta('vermelha', 'caloi', 2022, 800)
b2 = bicicleta('branca', 'BMX', 2020, 2000)

# Chamando a bicicleta e definindo algumas açôes:
#print(b1.cor, b1.modelo, b1.ano, b1.valor)
#b1.correr()
#b1.buzinar()
#b1.parar()
print(b1)
print(b2)
#b2.correr()

85991213538


    