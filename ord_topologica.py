from dados import *

class OrdenacaoTopologica:
    """Implementação do algoritmo de Kahn para ordenação topológica"""

    '''
        Baseado no pseudocódigo disponível em:
        https://en.wikipedia.org/wiki/Topological_sorting#Kahn.27s_algorithm
    '''

    L = None
    S = None

    def __init__(self):
        L = list()  # lista que irá conter os elementos ordenados
        S = set()  # conjunto de todos os vértices sem arestas de entrada

        for materia in g.V:
            if not materia.antecessores:  # se a matéria não tiver pré-requisito
                S.add(materia)

        while S:  # enquanto S é não vazio
            n = S.pop()  # remova um nodo n de S
            L.append(n)  # insira n em L

            for vertice in S



if __name__ == "__main__":
    OrdenacaoTopologica()
