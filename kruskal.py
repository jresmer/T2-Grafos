def kruskal(G):

    # árvore
    A = set()
    # subárvores
    S = [set(v) for v in G.vertices]
    # arestas (ordenadas)
    E_ = sorted(G.edges, key=G.w)

    for u, v in E_:

        if S[u] - S[v]:

            # adiciona a aresta a árvore
            A.add((u, v))
            # concatena Su e Sv
            x = S[u] + S[v]

            # atualiza as subárvores
            for y in x:
                S[y] = x

    return A
    