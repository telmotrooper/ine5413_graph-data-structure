from dados import g as curso
from dados_telmo import g as telmo
from ord_topologica import OrdenacaoTopologica

maximo = 28
contador_de_creditos = 0

print("{0} Ordenação topológica das matérias do curso {0}".format("-"*5))
OrdenacaoTopologica(curso).printar()

print("{0} Ordenação topológica das matérias do curso não cursadas pelo Telmo {0}".format("-"*5))
ot_telmo = OrdenacaoTopologica(telmo)

if not ot_telmo.ciclos:
    for vertice in ot_telmo.L.copy():
        contador_de_creditos += vertice.auxiliar
        if contador_de_creditos < maximo:
            print("{0} ({1} créditos)".format(vertice, vertice.auxiliar))
            ot_telmo.L.remove(vertice)
        else:
            print("-"*5)
            contador_de_creditos = 0
            print("{0} ({1} créditos)".format(vertice, vertice.auxiliar))
