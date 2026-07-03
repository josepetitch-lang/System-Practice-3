import sqlite3
DB_PATH = r"C:\Users\vikto\OneDrive\Documentos\Proyectos SQLITE\Teoría de SIstemas\sistemas.db"

def save_state_business(table, cicle, prod, cost, capital):
    query = f"INSERT INTO {table} VALUES (NULL, ?, ?, ?, ?)" 
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (cicle, prod, cost, capital))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al guardar en DB: {e}")