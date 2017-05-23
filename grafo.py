from vertice import Vertice


class Grafo:
    """Implementação da estrutura de dados grafo"""

    # Conjuntos
    v = set()
    a = set()

    # Contador de vértices
    num_vertices = 0

    def __init__(self):
        print("Grafo inicializado.")

    def adiciona_vertice(self):
        self.num_vertices += 1
        self.v.add(Vertice(self.num_vertices))

    def remove_vertice(self):
        print("To do!")

    def conecta(self):
        print("To do!")

    def desconecta(self):
        print("To do!")

    def ordem(self):
        print("To do!")

    def vertices(self):
        print("To do!")

    def um_vertice(self):
        print("To do!")

    def adjacentes(self):
        print("To do!")

    def grau(self):
        print("To do!")


if __name__ == "__main__":
    g = Grafo()
    g.adiciona_vertice()
