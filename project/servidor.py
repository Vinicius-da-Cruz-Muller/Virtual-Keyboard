import mysql.connector



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