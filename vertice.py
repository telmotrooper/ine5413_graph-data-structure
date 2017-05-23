class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = 0
    adjacentes = None

    def __init__(self):
        Vertice.numero += 1  # incrementa o contador de instâncias da classe
        self.numero = Vertice.numero  # atribui um número a esse vértice
        self.adjacentes = set()

    def __str__(self):
        return "Vértice {0}".format(self.numero)
        # return "Vértice {0} no endereço {1}".format(self.numero, hex(id(self)))

    def conecta(self, vertice):
        self.adjacentes.add(vertice)

    def desconecta(self, vertice):
        self.adjacentes.remove(vertice)
