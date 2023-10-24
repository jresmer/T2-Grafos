from grafo import DiGraph


def cfc(G):

    # primeira busca em profundidade
    A, F = dfs(G)

    print("A: {}".format(A))

    Gt = G.reversed()

    # # inicializa grafo sem vértices
    # Gt = DiGraph()

    # # adiciona os vértices de G a Gt
    # for label in G.get_labels():

    #     Gt.add_vetice(label)
    
    # # adiciona arestas inversas das arestas em A
    # for v, u in enumerate(A):

    #     if not u:
    #         continue

    #     Gt.add_edge((v+1, u))
    
    # busca em profundidade adaptada
    A = dfs_adapted(Gt, F)

    return A

def dfs_visit(G, v, C, F, A):
    
    # u é marcado como visitado
    C[v-1] = True

    print("vizinhos de {}: {}".format(v, G.neighbors(v)))

    for u in G.neighbors(v):

        #print("{} tentou aqui".format(v))

        if not C[u-1]:

            #print("{} passou aqui".format(v))

            A[u-1] = v
            dfs_visit(G, u, C, F, A)

    # insere u no início da "pilha"
    F.insert(0, v)

def dfs(G):

    n_vertices = len(G.vertices)

    # vértices visitados
    C = [False] * n_vertices
    # "pilha" F
    F = list()
    # antecessores
    A = [None] * n_vertices

    for u in G.vertices:

        if not C[u-1]:

            dfs_visit(G, u, C, F, A)
    
    return A, F

def dfs_adapted(G, F):

    n_vertices = len(G.vertices)

    print("Gt vertices: {}".format(list(G.vertices)))
    print("Gt edges: {}".format(list(G.edges)))
    print("pilha: {}".format(F))

    # vértices visitados
    C = [False] * n_vertices
    # antecessores
    A = [None] * n_vertices

    for u in F:

        if not C[u-1]:

            #print("{} passou".format(u))

            dfs_visit(G, u, C, F, A)

            print("A: {}".format(A))
    
    return A

def cfc_output(G):
    
    A = cfc(G)

    C = [False] * len(A)
    cfc_str = ""
    lines = list()

    for v, parent in enumerate(A):

        if not parent or C[v]:

            continue

        for line in lines: 

            if parent in line:

                line.append(v+1)
                C[v] = True
        
        if C[v]:

            continue
    
        C[v] = True
        lines.append([v+1])
        u = parent

        while u is not None and not C[u-1]:

            C[u-1] = True
            lines[-1].append(u)
            u = A[u-1]

    print(lines)

    for line in lines:

        for v in line:

            cfc_str += "{},".format(v)

        cfc_str = cfc_str[:-1] + "\n"

    if cfc_str == "":
        print("Não há componente fortemente conexa!")
    else:
        print(cfc_str[:-1] + ".")
