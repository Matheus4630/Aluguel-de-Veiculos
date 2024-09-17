from model.clientes import Clientes
from model.veiculos import Veiculos
from jsonS import AcessoLocacao


class Locacao:

    def newLocacao(self, lista=None):
        locacaos = AcessoLocacao().acessarLocacao()

        if not lista == None:
            locacaos[lista[2]] = lista[0], lista[1]
            AcessoLocacao().entradaDadosLocacao(locacaos)
            return

        Clientes().showClientes()
        C = int(input('Digite o ID do cliente que deseja um veiculo: '))
        cliente = Clientes().showClientes(C)

        print("Veiculos Disponivéis")
        Veiculos().showVeiculos()
        V = int(input('Digite o ID do veiculo: '))
        veiculo = Veiculos().showVeiculos(V)

        data = str(input("quando essa locação ocorrera (dia/mês/ano): "))
        locacaos[data] = cliente, veiculo

        AcessoLocacao().entradaDadosLocacao(locacaos)
        return

    def showLocacao(self, retorno=0):
        locacaos = AcessoLocacao().acessarLocacao()

        listaString = ''
        v = 0
        for locacao in locacaos:
            v = v + 1
            if retorno == 0:
                listaString += f"{l} - {locacao} - {locacaos[locacao]}\n"
            elif retorno == l:
                return locacao, locacaos[locacao]
        return listaString

    def editLocacao(self):
        locacaos = AcessoLocacao().acessarLocacao()
        self.showLocacao()

        id = int(input('Numero da Locação a Ser Editada: '))

        edit = self.showLocacao(id)

        newData = str(input('Data da Locação (dia/mês/ano): '))

        Clientes().showClientes()
        c = int(input('ID do cliente que deseja um veiculo: '))
        newCliente = Clientes().showClientes(c)

        Veiculos().showVeiculos()
        v = int(input('ID do Veiculo desejado: '))
        newVeiculo = Veiculos().showVeiculos(v)

        listaTemp = [newCliente, newVeiculo]

        if newData != edit:
            self.delLocacao(edit)
            listaTemp.append(newData)
            self.newLocacao(listaTemp)
            return

        locacaos[edit] = listaTemp
        AcessoLocacao().entradaDadosLocacao(locacaos)
        return

    def delLocacao(self, data=""):
        locacaos = AcessoLocacao().acessarLocacao()

        if data == "":
            self.showLocacao()

            id = int(input('Numero da Locação  a ser Deletada: '))
            delete = self.showLocacao(id)

            show = locacaos.pop(delete)
            print(f"{show} - Removido com Sucesso")

        elif data != "":
            del (locacaos[data])
            print(f'Data da Locação ({data}) atualizado, data anteior não correspondente a data atual')

        AcessoLocacao().entradaDadosLocacao(locacaos)
        return


# l = Locacao
# l().newLocacao()
