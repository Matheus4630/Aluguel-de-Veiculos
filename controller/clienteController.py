import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import DBManager
from model.validadorCPF import validate
import customtkinter

def receberDadosC(lista, mestre):
    lista = lista

    if validate(lista[3]):
        nome = lista[0]
        idade = lista[1]
        sexo = lista[2]
        cpf = lista[3]
        endereco = lista[4]
        capturarEnviar(nome, idade, sexo, cpf, endereco)
    else:
        janela = JanelaCPFInvalido(mestre)
        janela.mainloop()

def capturarEnviar(nome, idade, sexo, cpf, endereco):
    DBManager().criarUsuario(nome, idade, sexo, cpf, endereco)
    

def capturarMostrar():
    print(DBManager().listarUsuarios())
    return DBManager().listarUsuarios()
    

    

def capturarAtualizar(nome, idade, sexo, cpf, endereco):
    DBManager().atualizarUsuario(nome, idade, sexo, cpf, endereco)

def capturarDeletar(id):
    DBManager().deletarUsuario(id)


class JanelaCPFInvalido(customtkinter.CTk):

    def __init__(self, mestre):
        super().__init__()

        self.mestre = mestre
        self.title('CPF Invalido')
        self.geometry('300x200')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='CPF Invalido')
        self.label1.pack(padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, width=150, height=40, text='Tentar de Novo', command=self.erroCPF)
        self.button1.pack(padx=10, pady=10)

    def erroCPF(self):
        self.mestre.destroy()
        self.destroy()


# DBManager().capturarMostrar()