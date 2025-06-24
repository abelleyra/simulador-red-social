import tkinter as tk
from tkinter import messagebox, scrolledtext
import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo

    def eliminar(self, dato):
        actual = self.inicio
        anterior = None

        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        persona = []
        actual = self.inicio
        while actual:
            persona.append(actual.dato)
            actual = actual.siguiente
        return persona

class RedSocial:
    def __init__(self):
        self.usuarios = ListaEnlazada()

    def insertar(self, persona):
        self.usuarios.insertar(persona)

    def buscar(self, persona):
        return self.usuarios.buscar(persona)

    def eliminar(self, persona):
        return self.usuarios.eliminar(persona)

    def mostrar(self):
        return self.usuarios.mostrar()


red = RedSocial()


def agregar_usuario():
    nombre = entrada_nombre.get()
    try:
        edad = int(entrada_edad.get())
    except ValueError:
        messagebox.showerror("Error", "Edad debe ser un número entero.")
        return
    ciudad = entrada_ciudad.get()

    if not nombre or not ciudad:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        return

    persona = {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}
    red.insertar(persona)

    mostrar_usuarios()

def buscar_usuario():
    nombre = entrada_buscar.get()
    resultado = red.buscar(nombre)
    if resultado:
        messagebox.showinfo("Usuario encontrado", f"Nombre: {resultado['nombre']}\nEdad: {resultado['edad']}\nCiudad: {resultado['ciudad']}")
    else:
        messagebox.showwarning("No encontrado", f"El usuario '{nombre}' no está en la red.")

def eliminar_usuario():
    nombre = entrada_buscar.get()
    eliminado = red.eliminar(nombre)
    if eliminado:
        mostrar_usuarios()
        messagebox.showinfo("Eliminado", f"Usuario '{nombre}' eliminado correctamente.")
    else:
        messagebox.showwarning("No encontrado", f"El usuario '{nombre}' no fue encontrado.")
        
def mostrar_usuarios():
    usuarios = red.mostrar()
    texto_salida.delete(1.0, tk.END)
    for u in usuarios:
        texto_salida.insert(tk.END, f"Nombre: {u['nombre']}, Edad: {u['edad']}, Ciudad: {u['ciudad']}\n")

def mostrar_grafo():
    usuarios_list = red.usuarios.mostrar()
    if not usuarios_list:
        messagebox.showinfo("Info", "No hay usuarios para graficar.")
        return

    g = nx.Graph()
    g.add_nodes_from([(user['nombre'], user) for user in usuarios_list])

    nombres = [user['nombre'] for user in usuarios_list]
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            g.add_edge(nombres[i], nombres[j])

    plt.gcf().canvas.manager.set_window_title("Grafo de Red Social")
    node_labels = {
        user['nombre']: f"{user['nombre']}\nEdad: {user['edad']}\nCiudad: {user['ciudad']}"
        for user in usuarios_list
    }
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, labels=node_labels, node_size=3000, node_color='blue', font_size=8)
    plt.show()


ventana = tk.Tk()
ventana.title("Simulación de Red Social")
ventana.geometry("600x500")

tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

tk.Label(ventana, text="Ciudad:").pack()
entrada_ciudad = tk.Entry(ventana)
entrada_ciudad.pack()




tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario).pack(pady=10)
tk.Button(ventana, text="Mostrar Grafo", command=mostrar_grafo).pack(pady=10)

tk.Label(ventana, text="Buscar/Eliminar por Nombre:").pack()
entrada_buscar = tk.Entry(ventana)
entrada_buscar.pack()

tk.Button(ventana, text="Buscar Usuario", command=buscar_usuario).pack(pady=3)
tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario).pack(pady=3)


texto_salida = scrolledtext.ScrolledText(ventana, width=30, height=5)
texto_salida.pack(pady=10)

ventana.mainloop()
