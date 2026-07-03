import sqlite3


#
DB_OPERATIVA = (r"C:\Users\vikto\OneDrive\Documentos\Proyectos SQLITE\Teoría de SIstemas\sistemas.db")

def ejecutar_query(query, params = ()):
    try:
        with sqlite3.connect(DB_OPERATIVA) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Error de conexión: {e}. Revisa si la carpeta 'database' existe.")
        return []
    
def obtener_entorno(n_ciclo):
    query = "SELECT Factor_Demanda, Costo_Materia_Prima, Event FROM Entorno_Mercado WHERE ID_ENTORNO = ?"
    resultado = ejecutar_query(query, (n_ciclo,)) 
    return resultado[0] if resultado else (1.0, 50, "Estable")

def obtener_datos_sistemas(n_ciclo):
    query_est = "SELECT Ciclo, Produccion_FILA, Costo_Operativo, Capital_Restante FROM Empresa_Estatica WHERE Ciclo = ?"
    query_ada = "SELECT Ciclo, Produccion_Ajustada, Costo_Optimizado, Capital_Restante FROM Empresa_Adaptativa WHERE Ciclo = ?"
    
    cerrado = ejecutar_query(query_est, (n_ciclo-1,)) # Buscamos el capital del ciclo anterior
    abierto = ejecutar_query(query_ada, (n_ciclo-1,))
    
    if not cerrado or not abierto:
        return (n_ciclo-1, 100, 200, 1000), (n_ciclo-1, 100, 200, 1000)
        
    return cerrado[0], abierto[0]