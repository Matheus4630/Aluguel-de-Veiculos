#usar as telas aqui
from database import conexao
import telas

dbManager = conexao.DBManager()
dbManager.conectarBanco()
telas = telas.JanelaInicial()