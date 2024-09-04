from os.path import exists
import json



class JsonCliente:

    def __verificarCliente(self):
        '''verificador da existencia de json para cliente'''

        existencia = exists('clientes.json')
        return existencia

    def _manipularArquivoCliente(self):
        '''controlador de acesso json para cliente'''
        if self.__verificarCliente():
            conteudo = self.__lerArquivosCliente()
        else:
            conteudo = self.__criarArquivoCliente()
        return conteudo

    def __criarArquivoCliente(self):
        ''''''

        clientes = {}
        with open('clientes.json', 'w') as clientesVar:
            json.dump(clientes, clientesVar, indent=4)
        return clientes

    def __lerArquivosCliente(self):
        ''''''

        clientes = {}
        with open('clientes.json', 'r') as clientesVar:
            clientes = json.load(clientesVar)
        return clientes

    def _gravarArquivoCliente(self, conteudo):
        ''''''

        clientes = conteudo
        with open('clientes.json', 'w') as clientesVar:
            json.dump(clientes, clientesVar, indent=4)


class AcessoCliente(JsonCliente):

    def acessarClientes(self):
        clientes = self._manipularArquivoCliente()
        return clientes

    def entradaDadosClientes(self, clientes):
        self._gravarArquivoCliente(clientes)


class JsonVeiculo:

    def __verificarVeiculos(self):
        '''verificador da existencia de json para veiculo'''

        existencia = exists('veiculos.json')
        return existencia

    def _manipularArquivoVeiculo(self):
        '''controlador de acesso json para veiculos'''
        if self.__verificarVeiculos():
            conteudo = self.__lerArquivosVeiculo()
        else:
            conteudo = self.__criarArquivoVeiculo()
        return conteudo

    def __criarArquivoVeiculo(self):
        ''''''

        veiculos = {}
        with open('veiculos.json', 'w') as veiculosVar:
            json.dump(veiculos, veiculosVar, indent=4)
        return veiculos

    def __lerArquivosVeiculo(self):
        ''''''

        veiculos = {}
        with open('veiculos.json', 'r') as veiculosVar:
            veiculos = json.load(veiculosVar)
        return veiculos

    def _gravarArquivoVeiculo(self, conteudo):
        ''''''

        veiculos = conteudo
        with open('veiculos.json', 'w') as veiculosVar:
            json.dump(veiculos, veiculosVar, indent=4)


class AcessoVeiculo(JsonVeiculo):

    def acessarVeiculos(self):
        veiculos = self._manipularArquivoVeiculo()
        return veiculos

    def entradaDadosVeiculos(self, veiculos):
        self._gravarArquivoVeiculo(veiculos)


class JsonLocacao:

    def __verificarLocacao(self):
        '''verificador da existencia de json para locação'''

        existencia = exists('locacao.json')
        return existencia

    def _manipularArquivoLocacao(self):
        '''controlador de acesso json para locação'''
        if self.__verificarLocacao():
            conteudo = self.__lerArquivosLocacao()
        else:
            conteudo = self.__criarArquivoLocacao()
        return conteudo

    def __criarArquivoLocacao(self):
        ''''''

        locacao = {}
        with open('locacao.json', 'w') as locacaoVar:
            json.dump(locacao, locacaoVar, indent=4)
        return locacao

    def __lerArquivosLocacao(self):
        ''''''

        locacao = {}
        with open('locacao.json', 'r') as locacaoVar:
            locacao = json.load(locacaoVar)
        return locacao

    def _gravarArquivoLocacao(self, conteudo):
        ''''''

        locacao = conteudo
        with open('locacao.json', 'w') as locacaoVar:
            json.dump(locacao, locacaoVar, indent=4)


class AcessoLocacao(JsonLocacao):

    def acessarLocacao(self):
        locacaos = self._manipularArquivoLocacao()
        return locacaos

    def entradaDadosLocacao(self, locacao):
        self._gravarArquivoLocacao(locacao)

