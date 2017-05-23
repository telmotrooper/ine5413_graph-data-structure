import random
from vertice import Vertice


class Grafo:
    """Implementação da estrutura de dados grafo"""

    '''
    As complexidades das estruturas de dados padrão do Python estão disponíveis aqui:
    https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
    '''

    # Conjuntos
    V = None
    A = None

    def __init__(self):
        self.V = set()
        self.A = set()

    def adiciona_vertice(self, v):  # Complexidade O(1)
        self.V.add(v)

    # TODO: Implementar
    def remove_vertice(self):
        print()

    def conecta(self, v1, v2):  # Complexidade O(1)
        v1.conecta(v2)
        v2.conecta(v1)

    def desconecta(self, v1, v2):
        v1.desconecta(v2)
        v2.desconecta(v1)

    def ordem(self):  # Complexidade O(1)
        return len(self.V)

    def vertices(self):  # Complexidade O(1)
        return self.V

    # TODO: Pesquisar complexidade
    def um_vertice(self):
        return random.choice(tuple(self.V))

    def adjacentes(self, v):
        return v.adjacentes

    def grau(self, v):  # Complexidade O(1)
        return len(v.adjacentes)


if __name__ == "__main__":
    g = Grafo()
    v1 = Vertice()
    v2 = Vertice()
    v3 = Vertice()
    print()
    g.adiciona_vertice(v1)
    g.adiciona_vertice(v2)
    g.adiciona_vertice(v3)
    print()
    g.conecta(v1, v2)

    # g.adjacentes()

    print("O grafo é de ordem {0}.".format(g.ordem()))
