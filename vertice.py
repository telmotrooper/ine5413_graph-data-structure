class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = 0  # contador estático
    # adjacentes = None

    sucessores = None
    antecessores = None

    def __init__(self):
        Vertice.numero += 1  # incrementa o contador de instâncias da classe
        self.numero = Vertice.numero  # atribui um número a esse vértice
        # self.adjacentes = set()

        self.sucessores = set()
        self.antecessores = set()

    def __str__(self):
        # return "Vértice {0}".format(self.numero)
        return "Vértice {0} no endereço {1}".format(self.numero, hex(id(self)))

    def conecta(self, vertice):
        # self.adjacentes.add(vertice)
        self.sucessores.add(vertice)
        vertice.antecessores.add(self)

    def desconecta(self, vertice):
        # self.adjacentes.remove(vertice)
        self.sucessores.remove(vertice)
        vertice.antecessores.remove(self)
