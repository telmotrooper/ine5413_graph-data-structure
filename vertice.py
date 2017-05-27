class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = 0  # contador estático

    sucessores = None
    antecessores = None

    def __init__(self):
        Vertice.numero += 1  # incrementa o contador de instâncias da classe
        self.numero = Vertice.numero  # atribui um número a esse vértice

        self.sucessores = set()
        self.antecessores = set()

    def __str__(self):
        return "Vértice {0}".format(self.numero)
        # return "Vértice {0} no endereço {1}".format(self.numero, hex(id(self)))

    def conecta(self, vertice):
        self.sucessores.add(vertice)
        vertice.antecessores.add(self)

    def desconecta(self, vertice):
        self.sucessores.remove(vertice)
        vertice.antecessores.remove(self)
