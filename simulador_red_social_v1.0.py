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

    for i in range(3):

       red.insertar(persona={
        'nombre': input('ingrese nombre: '),
        'edad': int(input('ingrese edad:')) ,
        'ciudad': input('ciudad: ')
    })
    usuarios_list = red.usuarios.mostrar()
    g=nx.Graph()
    g.add_nodes_from([(user['nombre'], user) for user in usuarios_list])
    nombres = [user['nombre'] for user in usuarios_list]

    if len(nombres) > 1:
       g.add_edges_from([(nombres[0], nombres[1])])

    if len(nombres) > 2:
      g.add_edges_from([(nombres[0], nombres[2])])
      g.add_edges_from([(nombres[1], nombres[2])])

    plt.gcf().canvas.manager.set_window_title("grafo red")
    node_labels = {user['nombre']: f"nombre:{user['nombre']} \n edad:{user['edad']} \n ciudad: {user['ciudad']})" for user in usuarios_list}
    nx.draw(g, with_labels=True, labels=node_labels)
    plt.show()





