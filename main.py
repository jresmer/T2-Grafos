import sys
from componentes_fortemente_conexas import cfc_output
from kruskal import kruskal_output
from ordenacao_topologica import ot_output
from grafo import Graph, DiGraph
from utils import nextl

def read(file_path: str) -> Graph or DiGraph:

    with open(file_path) as f:

        lines = list(iter(f))

        # lê o número de vértices contidos no grafo
        n = int((list(lines)[0].split())[-1])
        # passa a primeira linha da lista
        nextl(lines)

        return Graph(lines, n) if lines[n].strip() == "*egdes" else DiGraph(lines, n)
    
def main():
    if __name__ == "__main__":
        
        if len(sys.argv) != 3:
            sys.exit("Usage: python3 main.py [Directory] [algorithm]")
        
        directory = sys.argv[1]
        algorith = sys.argv[2]

        G = read(directory)

        match algorith:

            # Componentes fortemente conexas
            case "1":
                cfc_output(G)
            # Ordenação topologica
            case "2":
                ot_output(G)
            # Árvore geradora mínima (Kruskal)
            case "3":
                kruskal_output(G)
            # Todos
            case _:
                cfc_output(G)
                ot_output(G)
                kruskal_output(G)

main()