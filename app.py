#usar as telas aqui
from database import conexao
from telas import JanelaInicial

def iniciarProjeto():
    dbManager = conexao.DBManager()
    dbManager.conectarBanco()
    telas = JanelaInicial()
