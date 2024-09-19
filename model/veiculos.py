from model.veiculo import Veiculo
from jsonS import AcessoVeiculo


class Veiculos:

    def newVeiculo(self, lista=None):
        veiculos = AcessoVeiculo().acessarVeiculos()

        if not lista == None:
            veiculoTemp = Veiculo(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
            veiculos[veiculoTemp.placa] = veiculoTemp.getVeiculo()
            AcessoVeiculo().entradaDadosVeiculos(veiculos)
            return

        marcaTemp = str(input('Marca: '))
        modeloTemp = str(input('Modelo: '))
        versaoTemp = str(input('Versao: '))
        motorTemp = str(input('Motor: '))
        corTemp = str(input('Cor: '))
        placaTemp = str(input("placa: "))

        veiculoTemp = Veiculo(marcaTemp, modeloTemp, versaoTemp, motorTemp, corTemp, placaTemp)
        veiculos[veiculoTemp.placa] = veiculoTemp.getVeiculo()

        AcessoVeiculo().entradaDadosVeiculos(veiculos)
        return

    def showVeiculos(self, retorno=0):
        veiculos = AcessoVeiculo().acessarVeiculos()
        # veiculos = DBManager().listarUsuarios()

        listaString = ''
        v = 0
        for veiculo in veiculos:
            v = v + 1
            if retorno == 0:
                listaString += f"{v} - {veiculo['Marca']} - {veiculo['Modelo']} - {veiculo['Versão']}\n"
            elif retorno == v:
                return veiculo, veiculos
        return listaString

    def editVeiculo(self):
        veiculos = AcessoVeiculo().acessarVeiculos()
        self.showVeiculos()

        numero = int(input('Numero do Veiculo a Ser Editado: '))

        edit, edits = self.showVeiculos(numero)

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
        AcessoVeiculo().entradaDadosVeiculos(veiculos)
        return

    def delVeiculo(self, placa=""):
        veiculos = AcessoVeiculo().acessarVeiculos()

        if placa == "":
            self.showVeiculos()

            numero = int(input('Numero do Veiculo a ser Deletado: '))
            delete, deletes = self.showVeiculos(numero)

            show = veiculos.pop(delete)
            print(f"{show} - Removido com Sucesso")

        elif placa != "":
            del (veiculos[placa])
            print(f'Indentificador do veiculo ({placa}) atualizado, placa anteior não correspondente a placa atual')

        AcessoVeiculo().entradaDadosVeiculos(veiculos)
        return

    def VerificarPlaca(self, placa):
        ''''''
        veiculos = AcessoVeiculo().acessarVeiculos()
        validar = True
        for c in veiculos.keys():
            if c == placa:  
                validar = False
                break  
        return validar


