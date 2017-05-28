class Vertice:
    """Implementação do vértice a ser utilizada com o grafo"""

    numero = 0  # contador estático
    etiqueta = None  # permite dar um nome ao vértice diferente do nome padrão
    auxiliar = None  # permite adicionar informações auxiliares ao vértice

    sucessores = None
    antecessores = None

    def __init__(self, etiqueta=None, auxiliar=None):
        Vertice.numero += 1  # incrementa o contador de instâncias da classe
        self.numero = Vertice.numero  # atribui um número a esse vértice
        self.etiqueta = etiqueta
        self.auxiliar = auxiliar

        self.sucessores = set()
        self.antecessores = set()

    def __str__(self):
        if self.etiqueta:
            return self.etiqueta
        else:
            return "Vértice {0}".format(self.numero)
            # return "Vértice {0} no endereço {1}".format(self.numero, hex(id(self)))

    def conecta(self, vertice):
        self.sucessores.add(vertice)
        vertice.antecessores.add(self)

    def desconecta(self, vertice):
        self.sucessores.remove(vertice)
        vertice.antecessores.remove(self)
