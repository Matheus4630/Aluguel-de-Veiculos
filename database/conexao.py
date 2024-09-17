import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        self.cursor = self.conn.cursor()

    def inserir_dados(self, coluna1, coluna2):
        query = "INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)"
        self.cursor.execute(query, (coluna1, coluna2))
        self.conn.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()