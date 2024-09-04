from clientes import Clientes
from veiculos import Veiculos
from jsonS import manipularArquivoLocacao, gravarArquivoLocacao


class Locacao:

    def __init__(self):
        pass

    def newLocacao(self):
        locacaos = manipularArquivoLocacao()

        Clientes().showClientes()
        C = int(input('Digite o ID do cliente que deseja um veiculo: '))
        cliente = Clientes().showClientes(C)

        print("Veiculos Disponivéis")
        Veiculos().showVeiculos()
        V = int(input('Digite o ID do veiculo: '))
        veiculo = Veiculos().showVeiculos(V)

        data = str(input("quando essa locação ocorrera (dia/mês/ano): "))
        locacaos[data] = cliente, veiculo

        gravarArquivoLocacao(locacaos)
        return


    def showLocacao(self):
        pass



    def editLocacao(self):
        pass



    def delLocacao(self):
        pass


l = Locacao
l().newLocacao()
