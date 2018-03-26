import sqlite3


class BancoDeDados:

    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        self.conexao.close

    def criar_tabelas(self):
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            );
            """)
        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def inserir_cliente(self, nome, cpf, email):
        try:
            cursor = self.conexao.cursor()

            try:
                cursor.execute("""
                    INSERT INTO clientes(nome, cpf, email) VALUES(?,?,?)
                """, (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe' % cpf)

            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def buscar_cliente(self, cpf):
        cursor = self.conexao.cursor()

        cursor.execute("""SELECT * FROM clientes;""")

        for linha in cursor.fetchall():
            if linha[2] == cpf:
                print('Cliente %s encontrado.' % linha[1])
                break
