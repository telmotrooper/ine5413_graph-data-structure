from dados.curso import g as curso
from dados.telmo import g as telmo
from dados.gustavo import g as gustavo
from ord_topologica import OrdenacaoTopologica

class Trabalho:
    """Onde a mágica acontece"""

    maximo = 28
    creditos = 0
    materias = None
    dependencias_validas = True

    def __init__(self):
        self.materias = set()

    def distribuir_disciplinas(self, lista_ordenada):
        for vertice in lista_ordenada:
            self.creditos += vertice.auxiliar

            # se algum dos antecessores do vértice está nesse
            # mesmo semestre, o vértice terá que ir para o próximo
            for antecessor in vertice.antecessores:
                if antecessor in self.materias:
                    self.dependencias_validas = False

            if self.creditos < self.maximo and self.dependencias_validas:
                self.materias.add(vertice)
                print("{0} ({1} créditos)".format(vertice, vertice.auxiliar))
            else:
                print("-" * 5)
                self.materias.clear()
                self.creditos = vertice.auxiliar
                print("{0} ({1} créditos)".format(vertice, vertice.auxiliar))

        # limpando os valores
        self.creditos = 0
        self.materias.clear()
        self.dependencias_validas = True

if __name__ == "__main__":
    print("{0} Ordenação topológica das matérias do curso {0}".format("-" * 5))
    OrdenacaoTopologica(curso).printar()

    t = Trabalho()

    print("{0} Ordenação topológica das matérias do curso não cursadas pelo Telmo (por semestre) {0}".format("-" * 5))
    t.distribuir_disciplinas(OrdenacaoTopologica(telmo).L)

    print("{0} Ordenação topológica das matérias do curso não cursadas pelo Gustavo (por semestre) {0}".format("-" * 5))
    t.distribuir_disciplinas(OrdenacaoTopologica(gustavo).L)
