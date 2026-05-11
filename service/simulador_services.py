from models.empresa import Empresa_Estatica, Empresa_Adaptativa
from models.entorno import Entorno
from database.db_service import obtener_datos_sistemas, obtener_entorno
from database.operaciones import save_state_business
from service.report_service import write_report

def correr_ciclo_simulacion(n_ciclo):
    
    f_dem, c_mat, nom_ev = obtener_entorno(n_ciclo)
    d_est, d_ada = obtener_datos_sistemas(n_ciclo)
    
    
    ambiente = Entorno(nom_ev, f_dem, c_mat)
    
    
    empresa_estatica = Empresa_Estatica(d_est[3], d_est[1], d_est[2]) 
    empresa_adaptativa = Empresa_Adaptativa(d_ada[3], d_ada[1], d_ada[2])
    
    
    cap_est = empresa_estatica.procesar_ciclo(ambiente)
    cap_ada, prod_ajustada = empresa_adaptativa.procesar_ciclo(ambiente)

    save_state_business("Empresa_Estatica", n_ciclo, empresa_estatica.produccion_fila, empresa_estatica.costo_operativo, cap_est)
    save_state_business("Empresa_Adaptativa", n_ciclo, prod_ajustada, empresa_adaptativa.costo_optimizado, cap_ada)

    mensaje = f"Ciclo {n_ciclo} | Evento: {nom_ev} | Cap.Est: {cap_est:.2f} | Cap Ada: {cap_ada:.2f}"
    write_report(mensaje)

    return {
    "n_ciclo": n_ciclo,
    "evento": nom_ev,
    "f_demanda": f_dem,
    "cantidad_material": c_mat,
    "capital_estatica": cap_est,
    "produccion_estatica": empresa_estatica.produccion_fila, 
    "produccion_adaptativa": prod_ajustada,
    "capital_adaptativa": cap_ada
   }

