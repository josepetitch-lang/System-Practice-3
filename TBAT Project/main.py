from service.simulador_services import correr_ciclo_simulacion
import time
import sys

def write_slowed(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def execute_tgs():
    print("UNEFA SERVICE: BIENVENIDOS... A LA MEJOR SIMULACIÓN JAMÁS VISTA :D")
    print()
    print("Autores: José Petit, José Guanipa, Jesús Guerra")
    time.sleep(5)
    print()
    print("SIMULADOR DE TEORÍA GENERAL DE SISTEMAS (TGS)\n")

    for i in range(1, 10):
       time.sleep(3)
       print(f" System: Analizando Ciclo Operativo {i}")
       time.sleep(5)

       try:
           data = correr_ciclo_simulacion(i)
           print()
           print()
           print("\n" + "="*50)
           print(f"\n Reporte de Entorno")
           print("="*50)
           write_slowed(f"Evento Detectado:{data['evento']}")
           print(f"Factor de Demanda: {data['f_demanda']}")
           print(f"Costo Materia: {data['cantidad_material']}")

           print(f"\n Comportamiento de los Subsistemas:")
           print()

          
           # EMPRESA ESTÁTICA: 
           time.sleep(3)
           print(f"Empresa Estática: Linked_Close (Sistema_Cerrado)")
           print(f"Decision: Producción invariable de ${data['produccion_estatica']}")
           write_slowed(f"Resultado: El capital cerró en ${data['capital_estatica']}")

           # EMPRESA ADAPTATIVA (ORION PA LOS PANAS ,SKSLKSLKSLKSKLSKLSKKLS)
           print(f"Empresa Adaptativa: ORION (Sistema_Abierto)")
           write_slowed(f"Decision: Ajuste en ORION, dinámico {data['produccion_adaptativa']}")
           time.sleep(4)
           print()
           write_slowed(f"Resutado: El capital cerró en ${data['capital_adaptativa']:.2f}")
           print("="*50)

           # RESULTADOS DE AMBASKDJKDJKDJDKJDKJDKDJKDJKDKD

           print(f"\n[3] Análisis de Eficiencia:")
           if data['capital_adaptativa'] > data['capital_estatica']:
               ganancia = data['capital_adaptativa'] - data['capital_estatica']
               write_slowed(f"El Sistema Abierto ha ganado por {ganancia:.2f}$, debido a su Homeostasis (Equilibrio pa los panas frescos xd)")
           else:
               write_slowed("El Sistema Cerrado resiste, pero su Entropía (Caos) no durará mucho")
       except Exception as e:
           print(f"Error: {e}: Problemas con la Simulación")
           continue

    time.sleep(5)
    print("FIN DE SIMULACIÓN... (Cargando reporte...)")
    time.sleep(5)
    print("Datos cargados en la databse y en reporte.txt")

    print("Veamos los datos necesarios")

    decision = input("¿Se logró el objetivo de demostrar la eficiencia del Sistema Abierto?(s/n):")
    if decision == "s":
               print("Listo: Sistema Abierto WINS")
    else:
               print("Bad luck. Try it next time")



if __name__ == "__main__":
    execute_tgs()


#for i in range(1, 10):
    #try:
     #   print(f"\n System: Analizando Ciclo Operativo {i}")
      #  time.sleep(1) # Bajamos el tiempo para que no sea eterno
      #  data = correr_ciclo_simulacion(i)
        
        # ... (todo tu código de print y write_slowed aquí adentro)
        
    #except Exception as e:
       # print(f" Salto en Ciclo {i}: {e}")
       # continue