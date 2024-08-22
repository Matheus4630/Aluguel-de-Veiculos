

class Veiculo:
    def __init__(self, marca, modelo, versao, motor, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.versao = versao
        self.motor = motor
        self.cor = cor
        self.placa = placa


    def getVeiculo(self):
        return self.marca, self.modelo, self.versao, self.motor, self.cor,self.placa


    def setVeiculo(self, marca, modelo, versao, motor, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.versao = versao
        self.motor = motor
        self.cor = cor
        self.placa = placa



