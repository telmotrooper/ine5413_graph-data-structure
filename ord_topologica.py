from dados import *

class OrdenacaoTopologica:
    """Implementação do algoritmo de Kahn para ordenação topológica"""

    '''
        Baseado no pseudocódigo disponível em:
        https://en.wikipedia.org/wiki/Topological_sorting#Kahn.27s_algorithm
    '''

    L = None
    S = None
    ciclos = False

    def __init__(self):
        self.L = list()  # lista que irá conter os elementos ordenados
        self.S = set()  # conjunto que irá conter todos os vértices sem arestas de entrada

        for vertice in g.V:
            if not vertice.antecessores:  # se o vértice não tiver antecessores
                self.S.add(vertice)

        while self.S:  # enquanto S é não vazio
            n = self.S.pop()  # remova um vértice n de S
            self.L.append(n)  # insira n em L

            for m in n.sucessores.copy():
                n.desconecta(m)  # remove a aresta do vértice
                if not m.antecessores:
                    self.S.add(m)

        # checa se o grafo contém ciclos
        for vertice in g.V:
            if vertice.sucessores or vertice.antecessores:
                self.ciclos = True
                break

if __name__ == "__main__":
    ordem = OrdenacaoTopologica()

    if ordem.ciclos:
        print("O grafo contém pelo menos um ciclo, logo é impossível obter uma ordenação topológica válida.")
    else:
        for vertice in ordem.L:
            print(vertice)
