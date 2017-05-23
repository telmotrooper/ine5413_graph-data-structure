class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = 0
    adjacentes = None

    def __init__(self):
        Vertice.numero += 1  # incrementa o contador de instâncias da classe
        self.numero = Vertice.numero  # atribui um número a esse vértice
        self.adjacentes = set()

    def conecta(self, vertice):
        self.adjacentes.add(vertice)
