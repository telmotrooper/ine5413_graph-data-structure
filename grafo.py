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
        for vertice in v.sucessores.copy():  # desconecta todos os sucessores
            v.desconecta(vertice)

        for vertice in v.antecessores.copy():  # desconecta todos os antecessores
            vertice.desconecta(v)

        self.V.remove(v)  # remove o vértice do grafo

    def conecta(self, v1, v2):  # Complexidade O(1)
        v1.conecta(v2)

    def desconecta(self, v1, v2):  # Complexidade O(1)
        v1.desconecta(v2)

    def ordem(self):  # Complexidade O(1)
        return len(self.V)

    def vertices(self):  # Complexidade O(1)
        return self.V

    def um_vertice(self):  # Complexidade O(1)
        temp = self.V.pop()
        self.V.add(temp)
        return temp

    def adjacentes(self, v):  # Complexidade O(n)
        return v.sucessores.union(v.antecessores)

    def sucessores(self, v):  # Complexidade O(1)
        return v.sucessores

    def antecessores(self, v):  # Complexidade O(1)
        return v.antecessores

    def grau(self, v):  # Complexidade O(1)
        return len(v.sucessores) + len(v.antecessores)

    def grau_de_emissao(self, v):  # Complexidade O(1)
        return len(v.sucessores)

    def grau_de_recepcao(self, v):  # Complexidade O(1)
        return len(v.antecessores)
