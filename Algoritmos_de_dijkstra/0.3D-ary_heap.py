# dijkstra con reconstruccion de ruta O de E log V
# que hace
#  calcula el costo minimo desde un origen y guarda el padre de cada nodo
# para que sirve
#  permite imprimir la ruta mas corta hasta un destino
# representacion
#  lista de adyacencia con pares (vecino, peso)
# requisito
#  pesos no negativos

import heapq  # cola de prioridad binaria

INF = 10**9  # infinito practico

def dijkstra_con_ruta(adj, origen):
    n = len(adj)                 # numero de nodos
    dist = [INF] * n             # distancias en infinito
    padre = [-1] * n             # padre[v] guarda desde que nodo llegue a v
    dist[origen] = 0             # origen arranca en cero
    pq = [(0, origen)]           # cola con tupla (costo, nodo)

    while pq:                    # procesa mientras haya candidatos
        d, u = heapq.heappop(pq) # saco el de menor costo
        if d != dist[u]:         # si esta viejo lo ignoro
            continue
        for v, w in adj[u]:      # reviso cada vecino v con peso w
            nd = d + w           # costo nuevo pasando por u
            if nd < dist[v]:     # mejora?
                dist[v] = nd     # actualizo costo
                padre[v] = u     # guardo que v viene de u
                heapq.heappush(pq, (nd, v))  # meto el nuevo par
    return dist, padre           # regreso costos y padres

def reconstruir_ruta(padre, origen, destino):
    ruta = []                    # aqui juntare los nodos de fin a inicio
    cur = destino                # empiezo en el destino
    while cur != -1:             # subo por los padres
        ruta.append(cur)
        if cur == origen:        # ya llegue al origen
            break
        cur = padre[cur]
    if ruta[-1] != origen:       # no hay camino
        return []                # regreso vacio
    ruta.reverse()               # volteo para que quede de origen a destino
    return ruta

def demo():
    # grafo ejemplo
    # 0-1:4  0-2:1  2-1:2  1-3:1  2-3:5
    adj = [
        [(1, 4), (2, 1)],            # 0
        [(0, 4), (2, 2), (3, 1)],    # 1
        [(0, 1), (1, 2), (3, 5)],    # 2
        [(1, 1), (2, 5)],            # 3
    ]
    origen = 0
    destino = 3
    dist, padre = dijkstra_con_ruta(adj, origen)   # corro dijkstra
    ruta = reconstruir_ruta(padre, origen, destino)  # armo la ruta

    print("distancias desde", origen, ":", dist)
    print("ruta a", destino, ":", ruta, "costo:", dist[destino])

if __name__ == "__main__":
    demo()