import psycopg2

class DBManager:
    def conectarBanco(self):
        try:
            # Conectando ao banco de dados PostgreSQL
            conn = psycopg2.connect(
            dbname='aluguelDeCarros',
            user='postgres',
            password='147885',
            host='localhost',
            port='5432'
            )

            # Criar um cursor para executar as consultas SQL
            cursor = conn.cursor()

    
          # Criar um cursor para executar as consultas SQL
            cursor = conn.cursor()

            # Escrever a consulta SQL
            consulta_sql = "SELECT * FROM usuarios"  # Exemplo: Selecionar todos os dados da tabela 'clientes'

            # Executar a consulta
            cursor.execute(consulta_sql)

            # Recuperar todos os dados retornados pela consulta
            resultados = cursor.fetchall()

            # Iterar sobre os resultados e exibir
            for linha in resultados:
                print(linha)

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erro ao acessar o banco de dados: {error}")

        finally:
            if conn:
                cursor.close()
                conn.close()
                print("Conexão com o banco de dados foi fechada.")




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

        # Chamar a função para buscar dados

#dbManager = DBManager()

# Chamando o método corretamente
#dbManager.conectarBanco()