import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import DBManager


def receberDadosV(lista):
    lista = lista
    marca = lista[0]
    modelo = lista[1]
    versao = lista[2]
    motor = lista[3]
    cor = lista[4]
    placa = lista[5]
    capturarEnviar(marca, modelo, versao, motor, cor, placa)
    

def capturarEnviar(marca, modelo, versao, motor, cor, placa):
    DBManager().criarVeiculo(marca, modelo, versao, motor, cor, placa)
    

def capturarMostrarV():
    print(DBManager().listarVeiculo())
    return DBManager().listarVeiculo()
    

    

def capturarAtualizarV(id, marca, modelo, versao, motor, cor, placa):
    DBManager().atualizarVeiculo(id, marca, modelo, versao, motor, cor, placa)

def capturarDeletarV(id):
    DBManager().excluirVeiculo(id)


