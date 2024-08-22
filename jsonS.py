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

manipularArquivoCliente()