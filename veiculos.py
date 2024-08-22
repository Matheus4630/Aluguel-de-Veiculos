from veiculo import Veiculo

veiculos = []
class Veiculos:

    def __init__(self, lista):
        self.lista = lista


    def newVeiculo(self):
        marcaTemp = str(input('Marca: '))
        modeloTemp = str(input('Modelo: '))
        versaoTemp = str(input('Versao: '))
        motorTemp = str(input('Motor: '))
        corTemp = str(input('Cor: '))

        veiculoTemp = Veiculo(marcaTemp, modeloTemp, versaoTemp, motorTemp, corTemp)

        self.lista.append(veiculoTemp)


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

        # self.lista[id].setVeiculo(newMarca, newModelo, newVersao, newMotor, newCor)
        temp = self.lista[id]
        temp.setCliente(newMarca, newModelo, newVersao, newMotor, newCor)


    def delVeiculo(self):
        self.showClientes()
        id = int(input('Numero do Veiculo a ser Deletado: '))
        id -= 1
        del (self.lista[id])

    
def CadastrarVeiculo():
    ''''''
    from jsonS import Motorista_manipular_arquivo, Motorista_gravar_arquivo
    motoristas = Motorista_manipular_arquivo()
    motorista = {}
    while True:
        CPF = str(input('Digite o CPF: ')).lstrip()
        if Verificar_CPF(CPF):
            motorista['CPF'] = CPF
            break
        else:
            print('CPF já cadastrado!')
    motorista['Nome'] = str(input('digite o nome: ')).title().lstrip()
    while True:
        carteira = str(input('Digite o tipo de Carteira de motorista: [A/B/AB] ')).upper().lstrip()
        if carteira in 'AB':
            motorista['Carteira'] = carteira
            break
        else:
            print('Digite uma categoria válida!')
    motoristas[CPF] = motorista
    print('motorista cadastrado com sucesso!')
    Motorista_gravar_arquivo(motoristas)