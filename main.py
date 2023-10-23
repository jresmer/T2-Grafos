import sys
from grafo import Graph, DiGraph

def read(file_path: str) -> Graph or DiGraph:

    with open(file_path) as f:

        lines = iter(f)

        # lê o número de vértices contidos no grafo
        n = int((lines[0].split())[-1])
        # passa a primeira linha da lista
        next(lines, None)

        return Graph(lines, n) if lines[n].strip() == "*egdes" else DiGraph(lines, n)
    
def main():
    if __name__ == "__main__":
        
        if len(sys.argv) != 2:
            sys.exit("Usage: python3 main.py [Directory]")
        
        directory = sys.argv[1]

        G = read(directory)
