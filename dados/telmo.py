from grafo import Grafo
from vertice import Vertice

g = Grafo()

# Fase 2
INE5405 = Vertice("Probabilidade e Estatística", 5)
MTM7174 = Vertice("Cálculo B para Computação", 4)

# Fase 3
INE5409 = Vertice("Cálculo Numérico para Computação", 4)

# Fase 4
INE5412 = Vertice("Sistemas Operacionais I", 4)
INE5413 = Vertice("Grafos", 4)
INE5415 = Vertice("Teoria da Computação", 4)

# Fase 5
INE5418 = Vertice("Computação Distribuída", 4)
INE5420 = Vertice("Computação Gráfica", 4)
INE5421 = Vertice("Linguagens Formais e Compiladores", 4)

# Fase 6
INE5424 = Vertice("Sistemas Operacionais II", 4)
INE5425 = Vertice("Modelagem e Simulação", 4)
INE5426 = Vertice("Construção de Compiladores", 4)
INE5427 = Vertice("Planejamento e Gestão de Projetos", 4)
INE5430 = Vertice("Inteligência Artificial", 4)
INE5453 = Vertice("Introdução ao Trabalho de Conclusão de Curso", 1)

# Fase 7
INE5429 = Vertice("Segurança em Computação", 4)
INE5431 = Vertice("Sistemas Multimídia", 4)
INE5432 = Vertice("Banco de Dados II", 4)
INE5433 = Vertice("Trabalho de Conclusão de Curso I", 0)

# Fase 8
INE5434 = Vertice("Trabalho de Conclusão de Curso II", 9)

# Pré-requisitos
MTM7174.conecta(INE5409)
INE5412.conecta(INE5418)
MTM7174.conecta(INE5420)
INE5415.conecta(INE5421)
INE5412.conecta(INE5424)
INE5405.conecta(INE5425)
INE5421.conecta(INE5426)
INE5405.conecta(INE5430)
INE5413.conecta(INE5430)
INE5427.conecta(INE5433)
INE5453.conecta(INE5433)
INE5433.conecta(INE5434)

# Adicionando os vértices no grafo
g.adiciona_vertice(INE5405)
g.adiciona_vertice(MTM7174)
g.adiciona_vertice(INE5409)
g.adiciona_vertice(INE5412)
g.adiciona_vertice(INE5413)
g.adiciona_vertice(INE5415)
g.adiciona_vertice(INE5418)
g.adiciona_vertice(INE5420)
g.adiciona_vertice(INE5421)
g.adiciona_vertice(INE5424)
g.adiciona_vertice(INE5425)
g.adiciona_vertice(INE5426)
g.adiciona_vertice(INE5427)
g.adiciona_vertice(INE5430)
g.adiciona_vertice(INE5453)
g.adiciona_vertice(INE5429)
g.adiciona_vertice(INE5431)
g.adiciona_vertice(INE5432)
g.adiciona_vertice(INE5433)
g.adiciona_vertice(INE5434)
