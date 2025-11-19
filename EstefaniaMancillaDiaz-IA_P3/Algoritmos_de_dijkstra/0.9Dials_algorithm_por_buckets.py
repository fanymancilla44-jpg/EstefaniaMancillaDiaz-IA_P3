# dials algorithm por buckets O de V por W mas E
# que hace
#  calcula costos minimos con pesos enteros chicos usando cubetas
# por que usarlo
#  si los pesos son enteros y chicos es muy rapido y simple
# requisitos
#  pesos enteros no negativos y el mayor peso debe ser pequeno
# representacion
#  lista de adyacencia con pares vecino y peso

INF = 10**9  # infinito practico

def dijkstra_dial(adj, origen, maxW):
    n = len(adj)                 # numero de nodos
    dist = [INF] * n             # distancias
    dist[origen] = 0             # origen en cero
    vis = [False] * n            # marcaje de fijos

    # cantidad de cubetas segun cota clasica
    B = maxW * n + 1
    buckets = [[] for _ in range(B)]  # lista de cubetas
    buckets[0].append(origen)         # origen en cubeta 0

    idx = 0                    # indice de cubeta actual
    procesados = 0             # cuantos nodos ya fijos

    while procesados < n:
        # avanzo hasta encontrar una cubeta con algo
        while idx < B and not buckets[idx]:
            idx += 1
        if idx >= B:
            break  # no hay mas alcanzables

        u = buckets[idx].pop()  # tomo un nodo de la cubeta actual
        if vis[u]:
            continue            # si ya fue fijado ignoro
        vis[u] = True
        procesados += 1

        # relajo aristas de u
        for v, w in adj[u]:
            if vis[v]:
                continue
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                # mando v a su cubeta segun distancia nueva
                if nd < B:
                    buckets[nd].append(v)
                else:
                    # si por alguna razon se pasa de B lo ignoro
                    # en grafos correctos con maxW esto no deberia pasar
                    pass
    return dist

def demo():
    # grafo no dirigido con pesos chicos entre 1 y 5
    # 0-1:4  0-2:1  2-1:2  1-3:1  2-3:5  3-4:3  4-5:2
    adj = [
        [(1,4),(2,1)],          # 0
        [(0,4),(2,2),(3,1)],    # 1
        [(0,1),(1,2),(3,5)],    # 2
        [(1,1),(2,5),(4,3)],    # 3
        [(3,3),(5,2)],          # 4
        [(4,2)],                # 5
    ]
    maxW = 5   # peso entero maximo del grafo
    origen = 0
    dist = dijkstra_dial(adj, origen, maxW)
    print("distancias desde", origen, ":", dist)

if __name__ == "__main__":
    demo()