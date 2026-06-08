import tkinter as tk
from tkinter import messagebox
import random
from states import PymeState
from events import dilemas_plan_do, ataques_aleatorios

class PlanDoGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PLAN DO: Cyber-SME Tycoon")
        self.root.geometry("750x630")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.state = PymeState()
        self.dilemas = list(dilemas_plan_do)
        random.shuffle(self.dilemas) 

        self.dilema_actual = None
        self.fase_ciclo = "decision"
        
        self.crear_componentes_interfaz()
        self.cargar_siguiente_turno()

    def crear_componentes_interfaz(self):
        """ Maquetacion limpia de la ventana principal utilizando Grid y Pack """
        
        self.panel_stats = tk.Frame(self.root, bg="#252538", bd=2, relief="groove")
        
        for i in range(4):
            self.panel_stats.grid_columnconfigure(i, weight=1)

        
        self.lbl_turno = tk.Label(self.panel_stats, text="Turno: 1", fg="#cdd6f4", bg="#252538", font=("Arial", 12, "bold"))
        self.lbl_turno.grid(row=0, column=0, pady=10)

        self.lbl_presupuesto = tk.Label(self.panel_stats, text="Presupuesto: $500", fg="#a6e3a1", bg="#252538", font=("Arial", 12, "bold"))
        self.lbl_presupuesto.grid(row=0, column=1, pady=10)

        self.lbl_seguridad = tk.Label(self.panel_stats, text="Seguridad: 30%", fg="#fab387", bg="#252538", font=("Arial", 11, "bold"))
        self.lbl_seguridad.grid(row=0, column=2, pady=10)

        self.lbl_cultura = tk.Label(self.panel_stats, text="Cultura DO: 20%", fg="#fab387", bg="#252538", font=("Arial", 11, "bold"))
        self.lbl_cultura.grid(row=0, column=3, pady=10)

        self.panel_pantalla = tk.Frame(self.root, bg="#313244", bd=1, relief="solid")
        self.panel_pantalla.pack(fill="both", expand=True, padx=15, pady=10)

        self.lbl_titulo_evento = tk.Label(self.panel_pantalla, text="Cargando Caso...", fg="#89b4fa", bg="#313244", font=("Arial", 14, "bold"), anchor="w")
        self.lbl_titulo_evento.pack(fill="x", padx=15, pady=(15, 5))

        self.txt_descripcion = tk.Text(self.panel_pantalla, fg="#cdd6f4", bg="#313244", font=("Arial", 11), wrap="word", bd=0, highlightthickness=0, selectbackground="#45475a")
        self.txt_descripcion.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_descripcion.config(state="disabled")

        self.panel_acciones = tk.Frame(self.root, bg="#1e1e2e")
        self.panel_acciones.pack(fill="x", padx=15, pady=(5, 10))

        
        self.frame_input = tk.Frame(self.panel_acciones, bg="#1e1e2e")
        self.frame_input.pack(pady=10)

        self.lbl_instruccion = tk.Label(self.frame_input, text="Ingresa tu opción (A / B):", fg="#cdd6f4", bg="#1e1e2e", font=("Arial", 11, "bold"))
        self.lbl_instruccion.pack(side="left", padx=10)

        self.entry_opcion = tk.Entry(self.frame_input, font=("Arial", 12, "bold"), width=5, justify="center", bg="#313244", fg="#cdd6f4", insertbackground="white")
        self.entry_opcion.pack(side="left", padx=10)
        self.entry_opcion.bind("<Return>", lambda e: self.validar_entrada_teclado()) # Vincular la tecla Enter física

        self.btn_confirmar = tk.Button(self.frame_input, text="Confirmar 🗲", bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold"), command=self.validar_entrada_teclado)
        self.btn_confirmar.pack(side="left", padx=10)

        self.btn_continuar = tk.Button(self.panel_acciones, text="Siguiente Paso ➔", bg="#89b4fa", fg="#11111b", font=("Arial", 11, "bold"), height=2, command=self.ejecutar_ciclo_juego)

        
        self.panel_creditos = tk.Frame(self.root, bg="#1e1e2e")
        self.panel_creditos.pack(fill="x", side="bottom", pady=(5, 5))

        self.lbl_creditos = tk.Label(self.panel_creditos, text="Desarrollado por: Equipo de Consultoría PLAN DO 💻", fg="#585b70", bg="#1e1e2e", font=("Arial", 9, "italic"))
        self.lbl_creditos.pack()

    def actualizar_tablero_visual(self):
        """ Actualiza los textos y los colores de la GUI segun las metricas """
        self.lbl_turno.config(text=f"Turno: {self.state.turno_actual}")
        self.lbl_presupuesto.config(text=f"Presupuesto: ${self.state.presupuesto}")
        
        
        seg = self.state.seguridad_red
        color_seg = "#f38ba8" if seg < 35 else ("#f9e2af" if seg < 65 else "#a6e3a1")
        self.lbl_seguridad.config(text=f"Seguridad: {seg}%", fg=color_seg)

        
        cul = self.state.cultura_pyme
        color_cul = "#f38ba8" if cul < 35 else ("#f9e2af" if cul < 65 else "#a6e3a1")
        self.lbl_cultura.config(text=f"Cultura DO: {cul}%", fg=color_cul)

    def imprimir_en_pantalla(self, titulo, texto, color_titulo="#89b4fa"):
        """ Escribe de forma limpia dentro de la caja de texto central """
        self.lbl_titulo_evento.config(text=titulo, fg=color_titulo)
        self.txt_descripcion.config(state="normal")
        self.txt_descripcion.delete("1.0", tk.END)
        self.txt_descripcion.insert(tk.END, texto)
        self.txt_descripcion.config(state="disabled")

    def cargar_siguiente_turno(self):
        """ Carga un dilema organizacional y limpia el campo de texto """
        self.actualizar_tablero_visual()
        
        if not self.dilemas or self.state.turno_actual > 3:
            self.finalizar_juego(victoria=True)
            return

        self.dilema_actual = self.dilemas.pop(0)
        
        texto_cuerpo = f"{self.dilema_actual['descripcion']}\n\n"
        texto_cuerpo += f"[A] - {self.dilema_actual['opciones'][0]['texto']}\n\n"
        texto_cuerpo += f"[B] - {self.dilema_actual['opciones'][1]['texto']}"
        
        self.imprimir_en_pantalla(self.dilema_actual["titulo"], texto_cuerpo)
        
        self.entry_opcion.config(state="normal")
        self.entry_opcion.delete(0, tk.END)
        self.entry_opcion.focus()
        
        self.frame_input.pack(pady=10)
        self.btn_continuar.pack_forget()
        self.fase_ciclo = "decision"

    def validar_entrada_teclado(self):
        """ Recoge el input, valida que sea A o B y ejecuta la decision """
        entrada = self.entry_opcion.get().strip().upper()
        
        if entrada == "A":
            self.frame_input.pack_forget()
            self.btn_continuar.pack(fill="x", expand=True)
            self.procesar_decision(0)
        elif entrada == "B":
            self.frame_input.pack_forget()
            self.btn_continuar.pack(fill="x", expand=True)
            self.procesar_decision(1)
        else:
            messagebox.showwarning("Entrada Inválida", "Por favor, ingresa únicamente la letra A o la letra B.")
            self.entry_opcion.delete(0, tk.END)

    def procesar_decision(self, indice_opcion):
        """ Aplica los cambios del dilema y muestra el feedback en la interfaz """
        opcion = self.dilema_actual["opciones"][indice_opcion]
        self.state.aplicar_impacto(opcion["impacto"])
        
        self.entry_opcion.config(state="disabled")
        self.actualizar_tablero_visual()

        if self.state.game_over:
            self.finalizar_juego(victoria=False)
            return

        titulo_feedback = f"Resultados: {self.dilema_actual['titulo']}"
        impactos_str = " | ".join([f"{k.replace('_', ' ').capitalize()}: {'+' if v>=0 else ''}{v}" for k, v in opcion["impacto"].items() if v != 0])
        cuerpo_feedback = f"{opcion['feedback']}\n\nImpacto en la Organización:\n[{impactos_str}]"
        
        self.imprimir_en_pantalla(titulo_feedback, cuerpo_feedback, color_titulo="#a6e3a1")
        self.fase_ciclo = "ataque"

    def ejecutar_ciclo_juego(self):
        """ Controla las fases intermedias mediante el boton de continuar """
        if self.fase_ciclo == "ataque":
            ataque = random.choice(ataques_aleatorios)
            exito, mensaje_ataque = self.state.procesar_ataque_aleatorio(ataque)
            
            color_titulo = "#a6e3a1" if exito else "#f38ba8"
            titulo_ataque = f"ALERTA DE INCIDENTE: Intento de {ataque['tipo']}"
            
            self.imprimir_en_pantalla(titulo_ataque, mensaje_ataque, color_titulo=color_titulo)
            self.actualizar_tablero_visual()

            if self.state.game_over:
                self.fase_ciclo = "game_over"
            else:
                self.state.avanzar_turno()
                self.fase_ciclo = "siguiente"
                
        elif self.fase_ciclo == "siguiente":
            self.cargar_siguiente_turno()
            
        elif self.fase_ciclo == "game_over":
            self.finalizar_juego(victoria=False)

    def finalizar_juego(self, victoria):
        """ Termina la ejecucion bloqueando controles y mostrando el estatus tecnico final """
        self.frame_input.pack_forget()
        self.btn_continuar.pack_forget()
        
        if victoria:
            titulo = "¡PROYECTO EXITOSO!"
            mensaje = f"Felicidades Consultor. Lograste estabilizar la operacion del abasto, capacitar al personal en Desarrollo Organizacional y aplicar las politicas basicas de conectividad corporativa.\n\nEstadisticas Finales de la PYME:\n- Presupuesto remanente: ${self.state.presupuesto}\n- Robustez de la Red: {self.state.seguridad_red}%\n- Cultura interna frente a Riesgos: {self.state.cultura_pyme}%"
            color = "#a6e3a1"
        else:
            titulo = "CRITICAL FAIL (Game Over)"
            mensaje = self.state.mensaje_final
            color = "#f38ba8"

        self.imprimir_en_pantalla(titulo, mensaje, color_titulo=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanDoGameApp(root)
    root.mainloop()