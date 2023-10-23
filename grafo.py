class Vertice:

    def __init__(self, index, label):
      self.__index = index
      self.__label = label

    @property
    def index(self):
      return self.__index

    @property
    def label(self):
      return self.__label

class Graph:

    def __init__(self, lines : list, n : int):
        self.__vertices = set()
        self.__edges = dict()
        self.__neighbors = None

        if lines:
            # inicializa a estrutura que mapeia os vizinhos
            self.__neighbors = [set()] * n

            # leitura dos vértices
            for _ in range(n):
                # lê uma linha
                v, label = lines[0].split()
                # adiciona um vértice ao seu conjunto V
                self.__vertices.add(Vertice(int(v), label))
                # passa uma linha
                next(lines, None)

            next(lines, None)

            self.__add_edges(lines)

    def __add_edges(self, lines):
      # leitura das arestas
      for u, v, w in lines:
              
          u, v, w = int(u), int(v), float(w)
          # adiciona a aresta (u, v) ao grafo
          self.__edges[frozenset(u, v)] = w
          # adiciona v aos vizinhos de u
          self.__neighbors[u].add(v)
          # adiciona u aos vizinhos de v
          self.__neighbors[v].add(u)

    def neighbors(self, u):
       return list(self.__neighbors[u])
    
    def w(self, u, v):
       
       if v in self.__neighbors[u]:
          return self.__edges[frozenset(u, v)]
       
    @property
    def vertices(self):
       return self.__vertices
    
    @property
    def edges(self):
       return self.__edges
       
class DiGraph(Graph):
    
    def __init__(self, lines):
       super().__init__(lines)

    def __add_edges(self, lines):
      # leitura dos arcos
      for u, v, w in lines:
              
          u, v, w = int(u), int(v), float(w)
          # adiciona o arco (u, v) ao grafo
          self.__edges[(u, v)] = w
          # adiciona v aos vizinhos de u
          self.__neighbors[u].add(v)
   
    def w(self, u, v):
       
       if v in self.__neighbors[u]:
          return self.__edges[(u, v)]
