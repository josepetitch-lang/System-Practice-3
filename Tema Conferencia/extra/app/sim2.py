import tkinter as tk
from sim1 import SimuladorComunicacion

class App:
    def __init__(self, root):
        self.sim = SimuladorComunicacion()
        self.root = root
        self.root.title("Simulador Python v1")
        
        self.label = tk.Label(root, text="Escribe tu mensaje:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.btn = tk.Button(root, text="Transmitir", command=self.ejecutar)
        self.btn.pack()
        
        self.resultado = tk.Label(root, text="")
        self.resultado.pack()

    def ejecutar(self):
        msg = self.entry.get()
        res = self.sim.procesar_mensaje(msg, 0.5)
        self.resultado.config(text=res)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()