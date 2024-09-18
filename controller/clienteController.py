from database.conexao import DBManager


def receberDadosC(lista):
    lista = lista
    nome = lista [0]
    idade = lista [1]
    sexo = lista [2]
    cpf = lista [3]
    endereco = lista [4]
    capturarEnviar(nome, idade, sexo, cpf, endereco)

def capturarEnviar(nome, idade, sexo, cpf, endereco):
    DBManager().criarUsuario(nome, idade, sexo, cpf, endereco)
    

def capturarMostrar():
    return DBManager().listarUsuarios()
    


def capturarAtualizar(nome, idade, sexo, cpf, endereco):
    DBManager().atualizarUsuario(nome, idade, sexo, cpf, endereco)

def capturarDeletar(id):
    DBManager().deletarUsuario(id)



DBManager().capturarMostrar()