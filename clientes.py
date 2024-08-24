from cliente import Cliente
from jsonS import manipularArquivoCliente, gravarArquivoCliente

class Clientes:
    def __init__(self):
        pass

    def newCliente(self):
        clientes = {}
        clientes = manipularArquivoCliente()

        nomeTemp = str(input('Nome: ')).lstrip()
        idadeTemp = str(input('Idade: ')).lstrip()
        sexoTemp = str(input('Sexo [M/F]: ')).lstrip().upper()
        cpfTemp = str(input('CPF: ')).lstrip()
        enderecoTemp = str(input('Endereco: ')).lstrip()


        clienteTemp = Cliente(nomeTemp, idadeTemp, sexoTemp, cpfTemp, enderecoTemp)
        print(clienteTemp, clienteTemp.getCliente())
        clientes[clienteTemp.nome] = clienteTemp.getCliente()
        print(clientes.items())

        gravarArquivoCliente(clientes)



        # motoristas = Motorista_manipular_arquivo()
        # motorista = {}
        # while True:
        #     CPF = str(input('Digite o CPF: ')).lstrip()
        #     if Verificar_CPF(CPF):
        #         motorista['CPF'] = CPF
        #         break
        #     else:
        #         print('CPF já cadastrado!')
        # motorista['Nome'] = str(input('digite o nome: ')).title().lstrip()
        # while True:
        #     carteira = str(input('Digite o tipo de Carteira de motorista: [A/B/AB] ')).upper().lstrip()
        #     if carteira in 'AB':
        #         motorista['Carteira'] = carteira
        #         break
        #     else:
        #         print('Digite uma categoria válida!')
        # motoristas[CPF] = motorista
        # print('motorista cadastrado com sucesso!')
        # Motorista_gravar_arquivo(motoristas)

    def showClientes(self):
        clientes = {}
        clientes = manipularArquivoCliente()
        c = 0
        for cliente in clientes:
            c = c + 1
            print(f"{c} - {cliente}")


    def editCliente(self):
        clientes = {}
        clientes = manipularArquivoCliente()
        self.showClientes()

        id = int(input('Numero do Cliente Que Sera Editado: '))
        id -= 1
        newName = str(input('Nome do Cliente: '))
        newIdade = float(input('Idade: '))
        newSexo = str(input('Sexo [M/F]: '))
        newCPF = str(input('Cofirmação de CPF do Cliente: '))
        newEndereco = str(input('Endereco do Cliente: '))

        #self.lista[id].setCliente(newName, newCPF)
        temp = self.lista[id]
        temp.setCliente(newName, newCPF)


    def delCliente(self):
        self.showClientes()
        id = int(input('Numero do Cliente Que Sera Deletado: '))
        id -= 1
        del(self.lista[id])


c = Clientes
c().newCliente()
