# dijkstra multi origen O de E log V
# que hace
#  calcula costos minimos desde varios nodos origen al mismo tiempo
# para que sirve
#  cuando tienes muchos puntos de partida y quieres el mas cercano para cada nodo
#  ejemplo varias estaciones o bases y quieres la mas cercana

import heapq  # cola de prioridad binaria

INF = 10**9  # infinito practico

def dijkstra_multi_origen(adj, origenes):
    n = len(adj)                 # numero de nodos
    dist = [INF] * n             # distancias iniciales
    padre = [-1] * n             # quien actualizo a cada nodo
    pq = []                      # cola de prioridad

    # inicializo todos los origenes con distancia cero
    for s in origenes:
        dist[s] = 0
        padre[s] = -1            # sin padre por ser fuente
        heapq.heappush(pq, (0, s))

    while pq:
        d, u = heapq.heappop(pq) # saco el menor
        if d != dist[u]:         # ignoro pares viejos
            continue
        for v, w in adj[u]:      # reviso vecinos
            nd = d + w           # costo nuevo pasando por u
            if nd < dist[v]:
                dist[v] = nd
                padre[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, padre

def reconstruir_camino(padre, fuentes_set, destino):
    # arma camino desde la fuente mas cercana hasta destino
    ruta = []
    cur = destino
    while cur != -1 and cur not in fuentes_set:
        ruta.append(cur)
        cur = padre[cur]
    if cur == -1:
        return []                # no hay camino a ninguna fuente
    ruta.append(cur)             # agrego la fuente
    ruta.reverse()
    return ruta

def demo():
    # grafo ejemplo no dirigido
    # 0-1:4  0-2:1  2-1:2  1-3:1  2-3:5  3-4:3  4-5:2
    adj = [
        [(1,4),(2,1)],          # 0
        [(0,4),(2,2),(3,1)],    # 1
        [(0,1),(1,2),(3,5)],    # 2
        [(1,1),(2,5),(4,3)],    # 3
        [(3,3),(5,2)],          # 4
        [(4,2)],                # 5
    ]
    origenes = [0, 5]            # dos fuentes al mismo tiempo
    dist, padre = dijkstra_multi_origen(adj, origenes)
    print("fuentes:", origenes)
    print("distancias:", dist)

    # ejemplo de reconstruccion al nodo 4
    fuentes_set = set(origenes)
    destino = 4
    ruta = reconstruir_camino(padre, fuentes_set, destino)
    print("ruta a", destino, ":", ruta, "costo", dist[destino])

if __name__ == "__main__":
    demo()
