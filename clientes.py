from cliente import Cliente

clientes = {}
class Clientes:
    def __init__(self, lista):
        self.lista = lista

    def newCliente(self):
        nomeTemp = str(input('Nome: '))
        cpfTemp = str(input('CPF: '))
        clienteTemp = Cliente(nomeTemp, cpfTemp)

        self.lista.append(clienteTemp)

    def showClientes(self):
        c = 0
        for cliente in self.lista:
            c = c + 1
            print(f"{c} - {cliente}")


    def editCliente(self):
        self.showClientes()
        id = int(input('Numero do Cliente Que Sera Editado: '))
        id -= 1
        newName = str(input('Nome do Cliente: '))
        newCPF = str(input('Cofirmação de CPF do Cliente: '))

        #self.lista[id].setCliente(newName, newCPF)
        temp = self.lista[id]
        temp.setCliente(newName, newCPF)


    def delCliente(self):
        self.showClientes()
        id = int(input('Numero do Cliente Que Sera Deletado: '))
        id -= 1
        del(self.lista[id])


