def kruskal(G):

    # árvore
    A = set()
    # subárvores
    S = [set()] * len(G.vertices)
    for v in G.vertices: S[v - 1] = set((v, ))
    # arestas (ordenadas)
    E_ = sorted(G.edges, key=G.w)

    for u, v in E_:

        if S[u-1] - S[v-1]:

            # adiciona a aresta a árvore
            A.add((u, v))
            # concatena Su e Sv
            x = S[u-1].union(S[v-1])

            # atualiza as subárvores
            for y in x:
                S[y-1] = x

    return A
    
def kruskal_output(G):

    total_cost = 0
    e_str = ""
    
    for u, v in kruskal(G):

        total_cost += G.w((u,v))

        e_str += "{}-{},".format(u, v)

    print(total_cost)
    print(e_str[:-1])
