from veiculo import Veiculo

veiculos = {}
class Veiculos:

    def __init__(self, lista):
        self.lista = lista

    @staticmethod
    def newVeiculo():
        marcaTemp = str(input('Marca: '))
        modeloTemp = str(input('Modelo: '))
        versaoTemp = str(input('Versao: '))
        motorTemp = str(input('Motor: '))
        corTemp = str(input('Cor: '))
        placaTemp = str(input("placa: "))

        veiculoTemp = {"Marca":marcaTemp, "Modelo":modeloTemp,"Versao": versaoTemp, "Motor":motorTemp,"Cor":corTemp, "Placa":placaTemp}
        return veiculoTemp

    def showVeiculos(self):
        v = 0
        for cliente in self.lista:
            v = v + 1
            print(f"{v} - {cliente}")


    def editVeiculo(self):
        self.showVeiculos()
        id = int(input('Numero do Veiculo a Ser Editado: '))
        id -= 1
        newMarca = str(input('Marca do Modelo: '))
        newModelo = str(input('Modelo do Veiculo: '))
        newVersao = str(input('Versao do Veiculo: '))
        newMotor = str(input('Motor do Veiculo: '))
        newCor = str(input('Cor do Veiculo: '))
        newPlaca = str(input('Placa do Veiculo: '))

        # self.lista[id].setVeiculo(newMarca, newModelo, newVersao, newMotor, newCor)
        temp = self.lista[id]
        temp.setCliente(newMarca, newModelo, newVersao, newMotor, newCor, newPlaca)


    def delVeiculo(self):
        self.showClientes()
        id = int(input('Numero do Veiculo a ser Deletado: '))
        id -= 1
        del (self.lista[id])


    def VerificarPlaca(placa):
        ''''''
        from jsonS import manipularArquivoVeiculo
        veiculos = manipularArquivoVeiculo()
        validar = True
        for c in veiculos.keys():
            if c == placa:  
                validar = False
                break  
        return validar
    
novo_veiculo = Veiculos.newVeiculo()

