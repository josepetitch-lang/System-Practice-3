import sqlite3

class DatabaseManager:
    def __init__(self, db_path = r"C:\Users\vikto\OneDrive\Documentos\Proyectos SQLITE\Teoría de SIstemas\sistemas.db"):
        self.db_path = db_path

    def conectar(self):
            return sqlite3.connect(self.db_path)
        
    def insertar_semila_tablas(self):
            with self.conectar() as conn:
                  cursor = conn.cursor()
                  cursor.execute("""INSERT OR IGNORE INTO Empresa_Estatica VALUES (0, 100, 25, 1000)""")
                  cursor.execute("""INSERT OR IGNORE INTO Empresa_Adaptativa VALUES (0, 100, 20, 100)""")
                  cursor.execute("""INSERT OR IGNORE INTO Entorno_Mercado VALUES (1,50, 'Estado Inicial')""")
                  conn.commit()
                  conn.close()