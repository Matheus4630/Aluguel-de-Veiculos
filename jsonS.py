from os.path import exists
import json



def verificarCliente():
    '''verificador da existencia de json para cliente'''

    existencia = exists('clientes.json')
    return existencia


def manipularArquivoCliente():
    '''controlador de acesso json para cliente'''
    if verificarCliente():
        conteudo = lerArquivosCliente()
    else:
        conteudo = criarArquivoCliente()
    return conteudo


def criarArquivoCliente():
    ''''''

    clientes = {}
    with open('clientes.json', 'w') as clientesVar:
        json.dump(clientes, clientesVar, indent=4)
    return clientes

def lerArquivosCliente():
    ''''''

    clientes = {}
    with open('clientes.json', 'r') as clientesVar:
        clientes = json.load(clientesVar)
    return clientes



def gravarArquivoCliente(conteudo):
    ''''''

    clientes = conteudo
    with open('clientes.json', 'w') as clientesVar:
        json.dump(clientes, clientesVar, indent=4)

def aleatorio():
    pass

# manipularArquivoCliente()

def verificarVeiculos():
    '''verificador da existencia de json para cliente'''

    existencia = exists('veiculos.json')
    return existencia

def manipularArquivoVeiculo():
    '''controlador de acesso json para cliente'''
    if verificarVeiculos():
        conteudo = lerArquivosVeiculo()
    else:
        conteudo = criarArquivoVeiculo()
    return conteudo


def criarArquivoVeiculo():
    ''''''

    veiculos = {}
    with open('veiculos.json', 'w') as veiculosVar:
        json.dump(veiculos, veiculosVar, indent=4)
    return veiculos

def lerArquivosVeiculo():
    ''''''

    veiculos = {}
    with open('veiculos.json', 'r') as veiculosVar:
        veiculos = json.load(veiculosVar)
    return veiculos



def gravarArquivoVeiculo(conteudo):
    ''''''

    veiculos = conteudo
    with open('veiculos.json', 'w') as veiculosVar:
        json.dump(veiculos, veiculosVar, indent=4)

# manipularArquivoVeiculo()






def verificarLocacao():
    '''verificador da existencia de json para locação'''

    existencia = exists('locacao.json')
    return existencia


def manipularArquivoLocacao():
    '''controlador de acesso json para locação'''
    if verificarCliente():
        conteudo = lerArquivosLocacao()
    else:
        conteudo = criarArquivoLocacao()
    return conteudo


def criarArquivoLocacao():
    ''''''

    locacao = {}
    with open('locacao.json', 'w') as locacaoVar:
        json.dump(locacao, locacaoVar, indent=4)
    return locacao

def lerArquivosLocacao():
    ''''''

    locacao = {}
    with open('locacao.json', 'r') as locacaoVar:
        locacao = json.load(locacaoVar)
    return locacao



def gravarArquivoLocacao(conteudo):
    ''''''

    locacao = conteudo
    with open('locacao.json', 'w') as locacaoVar:
        json.dump(locacao, locacaoVar, indent=4)

