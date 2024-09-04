from cliente import Cliente
from jsonS import manipularArquivoCliente, gravarArquivoCliente
import tkinter

class Clientes:
    def __init__(self):
        pass


    def newCliente(self, lista=None):
        clientes = manipularArquivoCliente()

        if not lista == None:
            clienteTemp = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4])
            clientes[clienteTemp.nome] = clienteTemp.getCliente()
            gravarArquivoCliente(clientes)
            return

        nomeTemp = str(input('Nome: ')).lstrip()
        idadeTemp = str(input('Idade: ')).lstrip()
        sexoTemp = str(input('Sexo [M/F]: ')).lstrip().upper()
        cpfTemp = str(input('CPF: ')).lstrip()
        enderecoTemp = str(input('Endereço: ')).lstrip()

        clienteTemp = Cliente(nomeTemp, idadeTemp, sexoTemp, cpfTemp, enderecoTemp)
        clientes[clienteTemp.nome] = clienteTemp.getCliente()

        gravarArquivoCliente(clientes)
        return


    def showClientes(self, retorno=0):
        clientes = manipularArquivoCliente()

        c = 0
        for cliente in clientes:
            c = c + 1
            if retorno == 0:
                print(f"{c} - {cliente}")
            elif retorno == c:
                return cliente


    def editCliente(self):
        clientes = manipularArquivoCliente()
        self.showClientes()

        id = int(input('Numero do Cliente Que Sera Editado: '))

        edit = self.showClientes(id)

        newName = str(input('Reescreva o Nome do Cliente: '))
        newIdade = str(input('Idade: '))
        newSexo = str(input('Sexo [M/F]: '))
        newCPF = str(input('Cofirmação de CPF do Cliente: '))
        newEndereco = str(input('Endereço do Cliente: '))

        listaTemp = [newName, newIdade, newSexo, newCPF, newEndereco]

        if newName != edit:
            self.delCliente(edit)
            self.newCliente(listaTemp)
            return

        clientes[edit] = listaTemp
        gravarArquivoCliente(clientes)
        return


    def delCliente(self, nome=''):
        clientes = manipularArquivoCliente()

        if nome == '':
            self.showClientes()

            id = int(input('Numero do Cliente Que Sera Deletado: '))
            delete = self.showClientes(id)

            show = clientes.pop(delete)
            print(f"{show} - Removido com Sucesso")

        elif nome != '':
            del clientes[nome]
            print(f'Indentificador do cliente ({nome}) atualizado, nome anteior não correspondente ao nome atual')

        gravarArquivoCliente(clientes)
        return



# c = Clientes
# c().newCliente()
# c().newCliente()
# c().newCliente()
# c().newCliente()
# c().editCliente()
# c().editCliente()
# c().delCliente()
# c().showClientes()



#

