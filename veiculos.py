from veiculo import Veiculo
from jsonS import manipularArquivoVeiculo, gravarArquivoVeiculo


class Veiculos:

    def __init__(self):
        pass


    def newVeiculo(self, lista=None):
        veiculos = manipularArquivoVeiculo()

        if not lista == None:
            veiculoTemp = Veiculo(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
            veiculos[veiculoTemp.placa] = veiculoTemp.getVeiculo()
            gravarArquivoVeiculo(veiculos)
            return

        marcaTemp = str(input('Marca: '))
        modeloTemp = str(input('Modelo: '))
        versaoTemp = str(input('Versao: '))
        motorTemp = str(input('Motor: '))
        corTemp = str(input('Cor: '))
        placaTemp = str(input("placa: "))

        veiculoTemp = Veiculo(marcaTemp, modeloTemp, versaoTemp, motorTemp, corTemp, placaTemp)
        veiculos[veiculoTemp.placa] = veiculoTemp.getVeiculo()

        gravarArquivoVeiculo(veiculos)
        return

    def showVeiculos(self, retorno=0):
        veiculos = manipularArquivoVeiculo()

        v = 0
        for veiculo in veiculos:
            v = v + 1
            if retorno == 0:
                print(f"{v} - {veiculo}")
            elif retorno == v:
                return veiculo


    def editVeiculo(self):
        veiculos = manipularArquivoVeiculo()
        veiculos = manipularArquivoVeiculo()
        self.showVeiculos()

        id = int(input('Numero do Veiculo a Ser Editado: '))

        edit = self.showVeiculos(id)

        newMarca = str(input('Marca do Modelo: '))
        newModelo = str(input('Modelo do Veiculo: '))
        newVersao = str(input('Versao do Veiculo: '))
        newMotor = str(input('Motor do Veiculo: '))
        newCor = str(input('Cor do Veiculo: '))
        newPlaca = str(input('Placa do Veiculo: '))

        listaTemp = [newMarca, newModelo, newVersao, newMotor, newCor, newPlaca]

        if newPlaca != edit:
            self.delVeiculo(edit)
            self.newVeiculo(listaTemp)
            return

        veiculos[edit] = listaTemp
        gravarArquivoVeiculo(veiculos)
        return


    def delVeiculo(self, placa=""):
        veiculos = manipularArquivoVeiculo()

        if placa == "":
            self.showVeiculos()

            id = int(input('Numero do Veiculo a ser Deletado: '))
            delete = self.showVeiculos(id)

            show = veiculos.pop(delete)
            print(f"{show} - Removido com Sucesso")

        elif placa != "":
            del (veiculos[placa])
            print(f'Indentificador do veiculo ({placa}) atualizado, placa anteior não correspondente a placa atual')

        gravarArquivoVeiculo(veiculos)
        return


    def VerificarPlaca(self, placa):
        ''''''
        veiculos = manipularArquivoVeiculo()
        validar = True
        for c in veiculos.keys():
            if c == placa:  
                validar = False
                break  
        return validar



# v = Veiculos
# v().newVeiculo()
# v().newVeiculo()
# v().showVeiculos()
# v().editVeiculo()
# v().editVeiculo()
# v().showVeiculos()
# v().delVeiculo()
# v().showVeiculos()
#
