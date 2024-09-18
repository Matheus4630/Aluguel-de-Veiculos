import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import DBManager
from model.validadorCPF import validate
from telas import JanelaCPFInvalido

def receberDadosC(lista, mestre):
    lista = lista

    if validate(lista[3]):
        nome = lista[0]
        idade = lista[1]
        sexo = lista[2]
        cpf = lista [3]
        endereco = lista[4]
        capturarEnviar(nome, idade, sexo, cpf, endereco)
    else:
        janela = JanelaCPFInvalido(mestre)
        janela.mainloop()

def capturarEnviar(nome, idade, sexo, cpf, endereco):
    DBManager().criarUsuario(nome, idade, sexo, cpf, endereco)
    

def capturarMostrar():
    return DBManager().listarUsuarios()

    

def capturarAtualizar(nome, idade, sexo, cpf, endereco):
    DBManager().atualizarUsuario(nome, idade, sexo, cpf, endereco)

def capturarDeletar(id):
    DBManager().deletarUsuario(id)



# DBManager().capturarMostrar()