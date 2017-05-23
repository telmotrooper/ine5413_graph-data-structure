import random
from vertice import Vertice


class Grafo:
    """Implementação da estrutura de dados grafo"""

    '''
    As complexidades das estruturas de dados padrão do Python estão disponíveis aqui:
    https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
    '''

    # Conjuntos
    v = set()
    a = set()

    # Contador de vértices
    num_vertices = 0

    def __init__(self):
        print("Grafo inicializado.")

    def adiciona_vertice(self):  # Complexidade O(1)
        self.num_vertices += 1
        self.v.add(Vertice(self.num_vertices))

    # TODO: Implementar
    def remove_vertice(self):
        print()

    def conecta(self, v1, v2):  # Complexidade O(1)
        v1.conecta(v2)
        v2.conecta(v1)

    # TODO: Implementar
    def desconecta(self):
        print()

    def ordem(self):  # Complexidade O(1)
        return len(self.v)

    # TODO: Implementar
    def vertices(self):
        print()

    # TODO: Pesquisar complexidade
    def um_vertice(self):
        return random.choice(tuple(self.v))

    # TODO: Implementar
    def adjacentes(self):
        print()

    # TODO: Implementar
    def grau(self):
        print()


if __name__ == "__main__":
    g = Grafo()
    g.adiciona_vertice()

    print("O grafo é de ordem {0}.".format(g.ordem()))
