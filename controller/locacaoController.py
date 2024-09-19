import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import DBManager

def receberDadosL(lista):
    lista = lista
    data = lista[0]
    cliente = lista[1]
    veiculo = lista[2]
    capturarEnviar(data, cliente, veiculo)
    

def capturarEnviar(data, cliente, veiculo):
    DBManager().criarLocacao(data, cliente, veiculo)
    

def capturarMostrar():
    print(DBManager().listarLocacao())
    return DBManager().listarLocacao()
    

def capturarAtualizarL(id, data, cliente, veiculo):
    DBManager().atualizarlocacao(id, data, cliente, veiculo)

def capturarDeletarL(id):
    DBManager().excluirLocacao(id)
