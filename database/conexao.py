import psycopg2

class DBManager:
    def conectarBanco(self):
        conn = psycopg2.connect(
        host="localhost",
        database="aluguelDeCarros",
        user="posgres",
        password="147885"
        )
        return conn

    def criar_usuario(self,nome, idade, sexo, cpf, endereço):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nome, idade, sexo, cpf, endereço) VALUES (%s, %s, %s,%s,%s)"
        cursor.execute(query, (nome, idade, sexo, cpf, endereço))
        conn.commit()
        cursor.close()
        conn.close()

    def listar_usuarios(self,):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
        
    def atualizar_usuario(self,id, novo_nome, novo_email, nova_idade):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, novo_email, nova_idade, id))
        conn.commit()
        cursor.close()
        conn.close()

    def excluir_usuario(self,id):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def criar_Veiculo(self,nome, idade, sexo, cpf, endereço):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nome, idade, sexo, cpf, endereço) VALUES (%s, %s, %s,%s,%s)"
        cursor.execute(query, (nome, idade, sexo, cpf, endereço))
        conn.commit()
        cursor.close()
        conn.close()

    def listar_usuarios(self,):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
        
    def atualizar_usuario(self,id, novo_nome, novo_email, nova_idade):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, novo_email, nova_idade, id))
        conn.commit()
        cursor.close()
        conn.close()

    def excluir_usuario(self,id):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()