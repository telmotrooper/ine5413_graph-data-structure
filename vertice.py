class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = None

    def __init__(self, numero):
        self.numero = numero
        print("Vértice {0} adicionado.".format(self.numero))
