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

    # TODO
    def remove_vertice(self):
        print()

    def conecta(self, v1, v2):  # Complexidade O(1)
        v1.conecta(v2)
        v2.conecta(v1)

    # TODO
    def desconecta(self):
        print("To do!")

    def ordem(self):
        return len(self.v)

    # TODO
    def vertices(self):
        print("To do!")

    # TODO
    def um_vertice(self):
        print("To do!")

    # TODO
    def adjacentes(self):
        print("To do!")

    # TODO
    def grau(self):
        print("To do!")


if __name__ == "__main__":
    g = Grafo()
    g.adiciona_vertice()

    print("O grafo é de ordem {0}.".format(g.ordem()))
