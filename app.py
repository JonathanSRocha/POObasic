class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, quantidade):
        self.velocidade += quantidade

    def frear(self, quantidade):
        self.velocidade -= quantidade

    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligado.")

    def desligar(self):
        print(f"O {self.marca} {self.modelo} está desligado.")

    def status(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")

# Criando um objeto da classe Carro
meu_carro = Carro("Ford", "Mustang", 2022, "Vermelho")

# Utilizando métodos e atributos do objeto
meu_carro.ligar()
meu_carro.acelerar(50)
meu_carro.status()
meu_carro.frear(10)
meu_carro.status()
meu_carro.desligar()
