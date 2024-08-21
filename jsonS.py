


def verificarCliente():
    '''verificador da existencia de json para cliente'''
    from os.path import exists

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
    import json

    clientes = {}
    with open('clientes.json', 'w') as clientesVar:
        json.dump(clientes, clientesVar, indent=4)
    return clientes

def lerArquivosCliente():
    ''''''
    import json

    clientes = {}
    with open('clientes.json', 'r') as clientesVar:
        clientes = json.load(clientesVar)
    return clientes



def gravarArquivoCliente(conteudo):
    ''''''
    import json

    clientes = conteudo
    with open('clientes.json', 'w') as clientesVar:
        json.dump(clientes, clientesVar, indent=4)

def aleatorio(testando):
     testando = testando
print("Funcionou e eu n sei fzr isso")

manipularArquivoCliente()