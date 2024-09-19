from model.cliente import Cliente
from jsonS import AcessoCliente
from database.conexao import DBManager 


class Clientes:

    def newCliente(self, lista=None):
        clientes = AcessoCliente().acessarClientes()

        if not lista == None:
            clienteTemp = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4])
            clientes[clienteTemp.cpf] = clienteTemp.getCliente()
            AcessoCliente().entradaDadosClientes(clientes)
            return

        nomeTemp = str(input('Nome: ')).lstrip()
        idadeTemp = str(input('Idade: ')).lstrip()
        sexoTemp = str(input('Sexo [M/F]: ')).lstrip().upper()
        cpfTemp = str(input('CPF: ')).lstrip()
        enderecoTemp = str(input('Endereço: ')).lstrip()

        clienteTemp = Cliente(nomeTemp, idadeTemp, sexoTemp, cpfTemp, enderecoTemp)
        clientes[clienteTemp.cpf] = clienteTemp.getCliente()

        AcessoCliente().entradaDadosClientes(clientes)
        return

    def showClientes(self, retorno=0):
        
        #clientes = AcessoCliente().acessarClientes()
        clientes = DBManager().listarUsuarios()
        listaString = ''
        c = 0
        for cliente in clientes:
            c = c + 1
            if retorno == 0:
                listaString += f"{cliente['id']} - {cliente['nome']} - {cliente['idade']} - {cliente['sexo']} \n"
            elif retorno == c:
                print(cliente, clientes)
                return cliente, clientes
        return listaString

    def editCliente(self):
        clientes = AcessoCliente().acessarClientes()
        self.showClientes()

        numero = int(input('Numero do Cliente Que Sera Editado: '))

        edit, edits = self.showClientes(numero)

        newName = str(input('Reescreva o Nome do Cliente: '))
        newIdade = str(input('Idade: '))
        newSexo = str(input('Sexo [M/F]: '))
        newCPF = str(input('Cofirmação de CPF do Cliente: '))
        newEndereco = str(input('Endereço do Cliente: '))

        listaTemp = [newName, newIdade, newSexo, newCPF, newEndereco]

        if newCPF != edit:
            self.delCliente(edit)
            self.newCliente(listaTemp)
            return

        clientes[edit] = listaTemp
        AcessoCliente().entradaDadosClientes(clientes)
        return

    def delCliente(self, cpf=''):
        clientes = AcessoCliente().acessarClientes()

        if cpf == '':
            self.showClientes()

            numero = int(input('Numero do Cliente Que Sera Deletado: '))
            delete, deletes = self.showClientes(numero)

            show = clientes.pop(delete)
            print(f"{show} - Removido com Sucesso")

        elif cpf != '':
            del clientes[cpf]
            print(f'Indentificador do cliente ({cpf}) atualizado, Indentificador anteior não correspondente ao atual')

        AcessoCliente().entradaDadosClientes(clientes)
        return



