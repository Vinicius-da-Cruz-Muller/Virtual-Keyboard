import mysql.connector
import datetime as datetime



class Servidor:
    def __init__(self):
        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            host="localhost",
            user="root",
            password="Semestre202301",
            database="users",
            pool_size=32,
        )
        self.cursor = None

    def conecta(self):
        try:
            mydb = self.pool.get_connection()
            self.cursor = mydb.cursor()
            return mydb

        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def buscarDados(self, tabela, coluna = "*", condicao = None):
        try:
            mydb = self.pool.get_connection()
            query = f"SELECT '{coluna}' FROM '{tabela}'"
            if condicao:
                query += f" WHERE '{condicao}'"
            self.cursor.execute(query)
            linhas = self.cursor.fetchall()
            mydb.close()
            return(linhas)
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
    

    def buscarDado(self, tabela, coluna=1, condicao=None):
        try:
            mydb = self.pool.get_connection()
            query = f"SELECT TOP 1 '{coluna}' FROM '{tabela}'"
            if condicao:
                query += f" WHERE '{condicao}'"
            self.cursor.execute(query)
            linhas = self.cursor.fetchall()
            mydb.close()
            return(linhas)
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")

    def inserirSessoes(self, hashEntrada, ordemNumeros):
        mydb = self.pool.get_connection()
        data_hora_atual = datetime.now()
        query = f"INSERT INTO Sessoes(hash, ordem, disponivel, ultima_vez_usado) VALUES ('{hashEntrada}', '{ordemNumeros}', 1, '{data_hora_atual}')"
        self.cursor.execute(query)
        self.cursor.commit()
        mydb.close()

    def AtualizarRegistro(self, tabela, colunas, condicao):
        try:
            mydb = self.pool.get_connection()
            query = f"UPDATE ´{tabela}' SET '{colunas}' WHERE '{condicao}'"
            self.cursor.execute(query)
            self.cursor.commit()
            mydb.close()
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")

    def LiberarSessoes(self):
        try:
            Ids = self.buscarDados("Sessoes", 'id', "disponivel = 0 and DATEADD(MINUTE, 10, ultima_vez_usado) < GETDATE()")
            for idRetornado in Ids:
                self.AtualizarRegistro('Sessoes', 'disponivel = 1', f"id = '{idRetornado[0]}'")
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")