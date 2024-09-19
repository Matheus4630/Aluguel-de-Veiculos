import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import DBManager

def receberDadosL(lista):
    lista = lista
    data = lista [0]
    cliente = lista [1]
    veiculo = lista [2]
    capturarEnviar(data, cliente, veiculo)
    

def capturarEnviar(data, cliente, veiculo):
    DBManager().criarLocacao(data, cliente, veiculo)
    

def capturarMostrar():
    print(DBManager().listarVeiculo())
    return DBManager().listarVeiculo()
    

def capturarAtualizar(data, cliente, veiculo):
    DBManager().atualizarUsuario(data, cliente, veiculo)

def capturarDeletar(id):
    DBManager().deletarUsuario(id)