from vertice import Vertice


class Grafo:
    """Implementação da estrutura de dados grafo"""

    '''
    As complexidades das estruturas de dados padrão do Python estão disponíveis aqui:
    https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
    '''

    V = None

    def __init__(self):
        self.V = set()

    def adiciona_vertice(self, v):  # Complexidade O(1)
        self.V.add(v)

    def remove_vertice(self, v):  # Complexidade O(n)
        for vertice in v.adjacentes:  # remove todas as arestas do vértice
            vertice.desconecta(v)

        self.V.remove(v)  # remove o vértice do grafo

    def conecta(self, v1, v2):  # Complexidade O(1)
        v1.conecta(v2)
        # v2.conecta(v1)

    def desconecta(self, v1, v2):  # Complexidade O(1)
        v1.desconecta(v2)
        # v2.desconecta(v1)

    def ordem(self):  # Complexidade O(1)
        return len(self.V)

    def vertices(self):  # Complexidade O(1)
        return self.V

    def um_vertice(self):  # Complexidade O(1)
        temp = self.V.pop()
        self.V.add(temp)
        return temp

    def adjacentes(self, v):  # Complexidade O(1)
        return v.adjacentes

    def grau(self, v):  # Complexidade O(1)
        return len(v.adjacentes)


if __name__ == "__main__":
    g = Grafo()
    v1 = Vertice()
    v2 = Vertice()
    v3 = Vertice()
    v4 = Vertice()
    v5 = Vertice()

    g.adiciona_vertice(v1)
    g.adiciona_vertice(v2)
    g.adiciona_vertice(v3)
    g.adiciona_vertice(v4)
    g.adiciona_vertice(v5)

    g.conecta(v1, v2)
    g.conecta(v1, v3)
    g.conecta(v1, v5)
    g.conecta(v2, v4)
    g.conecta(v3, v5)

    for vertice in g.adjacentes(v1):
        print("{0} é adjacente a {1}.".format(v1, vertice))

    print()

    for vertice in g.adjacentes(v2):
        print("{0} é adjacente a {1}.".format(v2, vertice))

    print()

    g.desconecta(v1, v2)

    for vertice in g.adjacentes(v1):
        print("{0} é adjacente a {1}.".format(v1, vertice))

    print()

    for vertice in g.adjacentes(v5):
        print("{0} é adjacente a {1}.".format(v5, vertice))

    print()

    g.remove_vertice(v1)

    for vertice in g.adjacentes(v5):
        print("{0} é adjacente a {1}.".format(v5, vertice))

    print()

    print("O grafo é de ordem {0}.".format(g.ordem()))

    print()

    for vertice in g.V:
        print(vertice)

    print("Qualquer: {0}".format(g.um_vertice()))

    for vertice in g.V:
        print(vertice)
