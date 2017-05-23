class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = 0
    adjacentes = set()

    def __init__(self, numero):
        self.numero = numero
        print("Vértice {0} adicionado.".format(self.numero))

    def conecta(self, vertice):
        self.adjacentes.add(vertice)
