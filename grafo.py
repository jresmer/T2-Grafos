from utils import nextl, split_st, split_nd

class Vertice:

    def __init__(self, index, label):
        self.__index = index
        self.__label = label

    def __str__(self) -> str:
        return "índice: {}, nome: {}".format(self.__index, self.__label)
       
    def __repr__(self) -> str:
        return "índice: {}, nome: {}".format(self.__index, self.__label)

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
        self.__V = None
        self.__neighbors = None

        if lines:
            # inicializa a estrutura que mapeia os vizinhos
            self.__neighbors = [set()] * n
            self.__V = [None] * n

            # leitura dos vértices
            for _ in range(n):
                # lê uma linha
                v, label = split_st(lines[0])
                # adiciona um vértice ao seu conjunto V
                self.__vertices.add(int(v))
                self.__V[int(v) - 1] = Vertice(int(v), label.strip()[1:-1])
                # passa uma linha
                nextl(lines)

            nextl(lines)

            self._add_edges(lines)

    def _add_edges(self, lines):
        # leitura das arestas
        for line in lines:
                
            u, v, w = split_nd(line)
            u, v, w = int(u), int(v), float(w)
            # adiciona a aresta (u, v) ao grafo
            self.__edges[frozenset((u, v))] = w
            # adiciona v aos vizinhos de u
            self.__neighbors[u-1].add(v)
            # adiciona u aos vizinhos de v
            self.__neighbors[v-1].add(u)

    def neighbors(self, u : int) -> list:
        return list(self.__neighbors[u - 1])
    
    def w(self, e : (int, int)) -> float:
        u, v = e
        
        if v in self.neighbors(u):
            return self.__edges[frozenset((u, v))]
        
        return float('inf')
    
    def vertice(self, v : int) -> Vertice:
        if v in self.__vertices:
            return self.__V[v-1]
        
        return None
       
    @property
    def vertices(self):
         return self.__vertices
    
    @property
    def edges(self):
        return (e for e in self.__edges)
       
class DiGraph(Graph):
    
    def __init__(self, lines : list, n : int):
        super().__init__(lines, n)

    def _add_edges(self, lines):
        # leitura dos arcos
        for line in lines:
                
            u, v, w = split_nd(line)
            u, v, w = int(u), int(v), float(w)
            # adiciona o arco (u, v) ao grafo
            self._Graph__edges[(u, v)] = w
            # adiciona v aos vizinhos de u
            if not self._Graph__neighbors[u-1]:
                self._Graph__neighbors[u-1] = set((v,))
            else:
                self._Graph__neighbors[u-1].add(v)
   
    def w(self, e : (int, int)) -> float:
        u, v = e
        
        if v in self.neighbors(u):
            return self._Graph__edges[(u, v)]
        
        return float('inf')
