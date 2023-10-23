from math import inf

def dfs_visit(G, u, C, T, F, time, O):
    
    # u é marcado como visitado
    C[u] = True
    # tempo é inclementado
    time += 1
    # tempo de início da visita em u é marcado em T
    T[u] = time

    for v in G.neighbors(u):

        if not C[v]:

            time = dfs_visit(G, v, C, T, F, time, O)
    
    time += 1

    # tempo do fim da visita em u é marcado em F
    F[u] = time
    # adiciona o vétice u ao início da lista
    O.insert(0, u)

    return time

def dfs(G):

    n_vertices = len(G.vertices)

    # vértices visitados
    C = [False] * n_vertices
    # tempo por vértice
    T = [inf] * n_vertices
    # _ por vértice
    F = [inf] * n_vertices
    # tempo de início
    time = 0
    # lista ordenada topologicamente
    O = list()

    for u in G.vertices:

        if not C[u]:

            time = dfs_visit(G, u, C, T, F, time, O)
    
    return O
