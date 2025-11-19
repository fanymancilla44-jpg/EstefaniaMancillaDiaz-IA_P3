# dijkstra con parada temprana O de E log V
# que hace
#  calcula el costo minimo desde origen hasta un destino y se detiene temprano
# por que usarlo
#  si solo te importa un destino ahorras trabajo al cortar cuando lo fijas
# requisitos
#  pesos no negativos
# representacion
#  lista de adyacencia con pares vecino y peso

import heapq  # cola de prioridad binaria

INF = 10**9  # infinito practico

def dijkstra_hasta_destino(adj, origen, destino):
    n = len(adj)                 # numero de nodos
    dist = [INF] * n             # distancias
    padre = [-1] * n             # para reconstruir ruta
    vis = [False] * n            # marcaje de fijos

    dist[origen] = 0
    pq = [(0, origen)]           # tuplas costo y nodo

    while pq:
        d, u = heapq.heappop(pq) # saco el menor
        if vis[u]:
            continue
        vis[u] = True            # fijo u

        if u == destino:         # parada temprana
            break

        for v, w in adj[u]:      # relajo u -> v
            if vis[v]:
                continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                padre[v] = u
                heapq.heappush(pq, (nd, v))

    return dist[destino], padre  # costo al destino y tabla padre

def reconstruir_ruta(padre, origen, destino):
    ruta = []
    cur = destino
    while cur != -1:
        ruta.append(cur)
        if cur == origen:
            break
        cur = padre[cur]
    if ruta[-1] != origen:
        return []
    ruta.reverse()
    return ruta

def demo():
    # grafo ejemplo no dirigido
    # 0-1:4  0-2:1  2-1:2  1-3:1  2-3:5
    adj = [
        [(1,4),(2,1)],          # 0
        [(0,4),(2,2),(3,1)],    # 1
        [(0,1),(1,2),(3,5)],    # 2
        [(1,1),(2,5)],          # 3
    ]
    origen = 0
    destino = 3
    costo, padre = dijkstra_hasta_destino(adj, origen, destino)
    ruta = reconstruir_ruta(padre, origen, destino)
    print("costo:", costo)
    print("ruta :", ruta)

if __name__ == "__main__":
    demo()