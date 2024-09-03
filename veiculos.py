
from veiculo import Veiculo
from jsonS import manipularArquivoVeiculo, gravarArquivoVeiculo

veiculos = {}
class Veiculos:
        def __init__(self):
            pass

        def newVeiculo(self, lista=None):
            veiculos = manipularArquivoVeiculo()

            if not lista == None:
                veiculoTemp = Veiculo(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
                veiculos[veiculoTemp.nome] = veiculoTemp.getCliente()
                gravarArquivoVeiculo(veiculos)
                return

            marcaTemp = str(input('Nome: ')).lstrip()
            modeloTemp = str(input('Idade: ')).lstrip()
            versaoTemp = str(input('Sexo [M/F]: ')).lstrip().upper()
            motorTemp = str(input('CPF: ')).lstrip()
            corTemp = str(input('Endereço: ')).lstrip()
            placaTemp = str(input('Placa: ')).lstrip()

            veiculoTemp = Veiculo(marcaTemp, modeloTemp, versaoTemp, motorTemp, corTemp, placaTemp)
            veiculos[veiculoTemp.placa] = veiculoTemp.getVeiculo()

            gravarArquivoVeiculo(Veiculos)
            return


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

        def delVeiculo(self, placa=''):
            veiculos = manipularArquivoVeiculo()

            if placa == '':
                self.showVeiculos()

                id = int(input('Numero do Cliente Que Sera Deletado: '))
                delete = self.showVeiculos(id)

                show = veiculos.pop(delete)
                print(f"{show} - Removido com Sucesso")

            elif placa != '':
                del veiculos[placa]
                print(f'Indentificador do cliente ({placa}) atualizado, nome anteior não correspondente ao nome atual')

            gravarArquivoVeiculo(veiculos)
            return

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
    

c = Veiculos
c().newVeiculo()
c().delVeiculo()
