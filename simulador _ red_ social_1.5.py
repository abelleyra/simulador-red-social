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
                print(f'El dato {dato} existe en la lista.')
                return True
            actual = actual.siguiente
        print(f'El dato {dato} no se encontró en la lista.')
        return False

    def mostrar(self):
        persona = []
        actual = self.inicio
        while actual:
            persona.append(actual.dato)
            actual = actual.siguiente
        return persona

class redSocial:
    def __init__(self):
        self.usuarios = ListaEnlazada()

    def insertar(self, persona):
        self.usuarios.insertar(persona)

    def buscar(self, persona):
        self.usuarios.buscar(persona)

    def eliminar(self, persona):
        self.usuarios.eliminar(persona)

    def mostrar(self):
        return self.usuarios.mostrar()

if __name__ == '__main__':
    red = redSocial()
    n = int(input("¿Cuántos usuarios deseas ingresar? "))
    for i in range (n):
     red.insertar(persona={
            'nombre': input('Ingrese nombre: '),
            'edad': int(input('Ingrese edad: ')),
            'ciudad': input('Ciudad: ')
        })

    usuarios_list = red.usuarios.mostrar()
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
    nx.draw(g, pos, with_labels=True, labels=node_labels, node_size=3000, node_color='lightblue', font_size=8)
    plt.show()





