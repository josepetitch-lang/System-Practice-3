from database.archivos import TXT_PATH

def write_report(message):
    try:
        with open(TXT_PATH, "a", encoding = "utf-8") as writh:
            writh.write(message + "\n")
    except FileNotFoundError:
        print("Archivo no encontrado")