from model.clientes import Clientes
from model.veiculos import Veiculos
from jsonS import AcessoLocacao
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import DBManager


class Locacao:

    def newLocacao(self, lista=None):
        #locacaos = AcessoLocacao().acessarLocacao()
        locacaos = DBManager().listarUsuarios()

        if not lista == None:
            locacaos[lista[0]] = lista[0], lista[1], lista[2]
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
        locacaos[data] = data, cliente, veiculo

        AcessoLocacao().entradaDadosLocacao(locacaos)
        return

    def showLocacao(self, retorno=0):
        #locacaos = AcessoLocacao().acessarLocacao()
        locacaos = DBManager().listarLocacao()

        listaString = ''
        l = 0
        for locacao in locacaos:
            l = l + 1
            if retorno == 0:
                listaString += f"{locacao['id']} - {locacao['data']} - {locacao['cliente']} - {locacao['veiculo']}\n"
            elif retorno == locacao['id']:
                return locacao, locacaos
        return listaString

    def editarLocacao(self):
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

        listaTemp = [newData, newCliente, newVeiculo]

        if newData != edit:
            self.delLocacao(edit)
            listaTemp.append(newData)
            self.newLocacao(listaTemp)
            return

        locacaos[edit] = listaTemp
        AcessoLocacao().entradaDadosLocacao(locacaos)
        return

    def deletarLocacao(self, data=""):
        #locacaos = AcessoLocacao().acessarLocacao()
        locacaos = DBManager().listarLocacao()

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


