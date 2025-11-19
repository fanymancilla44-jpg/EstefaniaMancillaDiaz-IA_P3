# dijkstra con cola de prioridad O de E log V
# que hace
#  calcula el costo minimo desde un nodo origen usando una cola de prioridad
# por que usarlo
#  es mas rapido que la version con matriz cuando el grafo es grande o disperso
# requisitos
#  pesos no negativos
# representacion
#  usamos lista de adyacencia con pares vecino y peso

import heapq  # libreria de python para manejar la cola de prioridad binaria

INF = 10**9  # valor grande para simular infinito

def dijkstra_heap(adj, origen):
    n = len(adj)                 # numero de nodos segun el tamaño de la lista
    dist = [INF] * n             # arreglo de distancias inicial en infinito
    dist[origen] = 0             # distancia del origen es cero
    pq = [(0, origen)]           # cola de prioridad con tupla costo y nodo

    while pq:                    # mientras haya candidatos en la cola
        d, u = heapq.heappop(pq) # saco el nodo con menor costo actual
        if d != dist[u]:         # si el par esta desactualizado lo ignoro
            continue
        for v, w in adj[u]:      # recorro vecinos v con peso w
            nd = d + w           # costo nuevo pasando por u
            if nd < dist[v]:     # si mejora la distancia a v
                dist[v] = nd     # guardo la nueva distancia
                heapq.heappush(pq, (nd, v))  # meto el par nuevo a la cola
    return dist                  # regreso todas las distancias finales

def demo():
    # grafo ejemplo como lista de adyacencia
    # 0-1:4  0-2:1  2-1:2  1-3:1  2-3:5
    adj = [
        [(1, 4), (2, 1)],   # vecinos de 0
        [(0, 4), (2, 2), (3, 1)],  # vecinos de 1
        [(0, 1), (1, 2), (3, 5)],  # vecinos de 2
        [(1, 1), (2, 5)],   # vecinos de 3
    ]
    origen = 0
    dist = dijkstra_heap(adj, origen)
    print("distancias desde", origen, ":", dist)

if __name__ == "__main__":
    demo()