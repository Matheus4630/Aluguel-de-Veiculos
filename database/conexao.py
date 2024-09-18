import psycopg2

class DBManager:
    def conectarBanco(self):
        conn = psycopg2.connect(
        host="localhost",
        database="aluguelDeCarros",
        user="postgres",
        password="147885"
        )
        return conn

    def criarUsuario(self,nome, idade, sexo, cpf, endereço):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nome, idade, sexo, cpf, endereço) VALUES (%s, %s, %s,%s,%s)"
        cursor.execute(query, (nome, idade, sexo, cpf, endereço))
        conn.commit()
        cursor.close()
        conn.close()


    def listarUsuarios(self):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
    

        
    def atualizarUsuario(self,id, novo_nome, novo_email, nova_idade):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, novo_email, nova_idade, id))
        conn.commit()
        cursor.close()
        conn.close()

    def excluirUsuario(self,id):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def criarVeiculo(self,nome, idade, sexo, cpf, endereço):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nome, idade, sexo, cpf, endereço) VALUES (%s, %s, %s,%s,%s)"
        cursor.execute(query, (nome, idade, sexo, cpf, endereço))
        conn.commit()
        cursor.close()
        conn.close()

    def listar_veiculo(self,):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
        
    def atualizar_veiculo(self,id, novo_nome, novo_email, nova_idade):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, novo_email, nova_idade, id))
        conn.commit()
        cursor.close()
        conn.close()

    def excluir_veiculo(self,id):
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

