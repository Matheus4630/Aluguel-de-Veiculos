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
    

        
    def atualizarUsuario(self,id, nome, idade, sexo, cpf, endereço):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET nome = %s, idade = %s, sexo = %s, cpf = %s, endereco = %s  WHERE id = %s"
        cursor.execute(query, (nome, idade, sexo, cpf, endereço, id))
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

    def criarVeiculo(self,marca, modelo, versao, motor, cor, placa):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "INSERT INTO veiculos (marca, modelo, versao, motor, cor, placa) VALUES (%s, %s, %s,%s,%s, %s)"
        cursor.execute(query, (marca, modelo, versao, motor, cor, placa))
        conn.commit()
        cursor.close()
        conn.close()

    def listarVeiculo(self):
        conn = self.conectarBanco()
    

        if conn is None:
            print("Falha ao conectar ao banco de dados.")
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM veiculos")
        rows = cursor.fetchall()
    
        cursor.close()
        conn.close()
        
        veiculos = []
        for row in rows:
            veiculo = {
            "id": row[0],
            "marca": row[1],
            "modelo": row[2],
            "versao": row[3],
            "motor": row[4],
            "cor": row[5],
            "placa": row[6]
        }
            veiculos.append(veiculo)

        return veiculos
        
    def atualizarVeiculo(self,id, marca, modelo, versao, motor, cor, placa):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE veiculos SET marca = %s, modelo = %s, versao = %s, motor = %s, cor = %s, placa = %s WHERE id = %s"
        cursor.execute(query, (marca, modelo, versao, motor, cor, placa, id))
        conn.commit()
        cursor.close()
        conn.close()

    def excluirVeiculo(self,id):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "DELETE FROM veiculo WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def criarLocacao(self, data, cliente, veiculo):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "INSERT INTO locacaos (data, cliente, veiculo) VALUES (%s, %s, %s)"
        cursor.execute(query, (data, cliente, veiculo))
        conn.commit()
        cursor.close()
        conn.close()

    def listarLocacao(self):
        conn = self.conectarBanco()
    

        if conn is None:
            print("Falha ao conectar ao banco de dados.")
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM locacaos")
        rows = cursor.fetchall()
    
        cursor.close()
        conn.close()
        
        locacaos = []
        for row in rows:
            locacao = {
            "id": row[0],
            "marca": row[1],
            "modelo": row[2],
            "versao": row[3],
            "motor": row[4],
            "cor": row[5],
            "placa": row[6]
        }
            locacaos.append(locacao)

        return locacaos
        
    def atualizarlocacao(self,id, data, cliente, veiculo):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "UPDATE locacaos SET data = %s, cliente = %s, veiculo = %s WHERE id = %s"
        cursor.execute(query, (data, cliente, veiculo, id))
        conn.commit()
        cursor.close()
        conn.close()

    def excluirLocacao(self,id):
        conn = self.conectarBanco()
        cursor = conn.cursor()
        query = "DELETE FROM locacaos WHERE id = %s"
        cursor.execute(query, (id))
        conn.commit()
        cursor.close()
        conn.close()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()

        # Chamar a função para buscar dados

dbManager = DBManager()

# Chamando o método corretament
#dbManager.conectarBanco()
#print(dbManager.listarUsuarios())
#dbManager.atualizarUsuario(3, 'Joao','15','M','111.111.111-11', 'Rua')
#print(dbManager.listarUsuarios())
