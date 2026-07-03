import tkinter as tk
from tkinter import messagebox

def analizar():
    mensaje = entry.get()
    ruido_comun = ["eh", "bueno", "o sea", "básicamente", "no sé"]
    palabras = mensaje.lower().split()
    total = len(palabras)
    ruido = [p for p in palabras if p in ruido_comun]
    porcentaje = (len(ruido) / total * 100) if total > 0 else 0
    
    resultado = f"Ruido: {porcentaje:.2f}%"
    messagebox.showinfo("Reporte TBAT", resultado + "\nEstado: " + ("Óptimo" if porcentaje < 10 else "Alerta"))

root = tk.Tk()
root.title("Analizador TBAT")
root.geometry("300x150")

entry = tk.Entry(root)
entry.pack(pady=20)

btn = tk.Button(root, text="Analizar Mensaje", command=analizar)
btn.pack()

root.mainloop()