import tkinter as tk

class Application():
    hostsFile = "C:/Windows/System32/drivers/etc/hosts"

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x150")
        self.window.title("Bloqueador de Páginas")
        self.window.resizable(width=False, height=False)
        self.createLabel()
        self.createEntry()
        self.boton_crear()
        self.boton_eliminar()
        self.boton_listar()
        self.window.mainloop()

    def createLabel(self):
        self.label = tk.Label(self.window, text="Ingresa URL:")
        self.label.pack(pady=5)

    def createEntry(self):
        self.entry = tk.Entry(self.window, width=30)
        self.entry.pack()

    def boton_crear(self):     
        self.addButton = tk.Button(self.window, text="Añadir", command=self.agregar_url)
        self.addButton.pack(pady=5)

    def boton_eliminar(self):     
        self.removeButton = tk.Button(self.window, text="Eliminar", command=self.eliminar_url)
        self.removeButton.pack(pady=5)
        
    def boton_listar(self):
        self.addButton = tk.Button(self.window, text="Listar", command=self.listar_url)
        self.addButton.pack(pady=5)



    def agregar_url(self):
        url = self.entry.get()
        if url:
            with open(self.hostsFile, 'a') as file:
                file.write(f"\n127.0.0.1\t www.{url}.com")
            self.entry.delete(0, tk.END)  

    

    def eliminar_url(self):
        url = self.entry.get()
        if url:
            with open(self.hostsFile, 'r') as file:
                lines = file.readlines()
            with open(self.hostsFile, 'w') as file:
                for line in lines:
                    if not line.strip().endswith(f"www.{url}.com"):
                        file.write(line)
            self.entry.delete(0, tk.END)  

    def listar_url(self):
        new_window = tk.Tk()
        new_window.geometry("400x400")
        new_window.title("Páginas Bloqueadas")
        new_window.resizable(width=False, height=False)
        with open(self.hostsFile, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().startswith("127.0.0.1\t www."):
                    label = tk.Label(new_window, text=line.strip())
                    label.pack(pady=5)

        new_window.mainloop()

app = Application()
