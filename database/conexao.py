import psycopg2

class DBManager:
    def __init__(self):
        self.dbname = 'aluguelDeCarros'  # Nome correto do banco de dados
        self.user = 'postgres'          # Usuário correto
        self.password = '147885'        # Senha correta
        self.host = 'localhost'        # Host (para ambiente local, 'localhost')
        self.port = '5432'             # Porta do PostgreSQL (geralmente 5432)

    def conectarBanco(self):
        try:
            # Tenta estabelecer uma conexão com o banco de dados
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn  # Retorna a conexão válida
        except psycopg2.DatabaseError as error:
            # Se ocorrer um erro de banco de dados, exibe o erro e retorna None
            print(f"Erro ao conectar ao banco de dados: {error}")
            return None


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
    

        if conn is None:
            print("Falha ao conectar ao banco de dados.")
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
    
        cursor.close()
        conn.close()
        
        usuarios = []
        for row in rows:
            usuario = {
            "id": row[0],
            "nome": row[1],
            "idade": row[2],
            "sexo": row[3],
            "cpf": row[4],
            "endereco": row[5]
        }
            usuarios.append(usuario)

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

        # Chamar a função para buscar dados

#dbManager = DBManager()

# Chamando o método corretamente
#dbManager.conectarBanco()