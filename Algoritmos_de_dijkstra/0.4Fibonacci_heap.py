# dijkstra paso a paso con cola de prioridad O de E log V
# que hace
#  calcula costos minimos y va mostrando en consola cada paso clave
# para que sirve
#  ayuda a entender como se elige el nodo y como se relajan las aristas
# representacion
#  lista de adyacencia con pares vecino y peso
# requisito
#  pesos no negativos

import heapq  # cola de prioridad binaria

INF = 10**9  # infinito practico

def dijkstra_paso_a_paso(adj, origen):
    n = len(adj)                 # cantidad de nodos
    dist = [INF] * n             # distancias iniciales
    dist[origen] = 0             # origen en cero
    vis = [False] * n            # marca de fijo
    pq = [(0, origen)]           # cola con costo y nodo

    paso = 0                     # contador de pasos para imprimir

    print("inicio desde", origen)
    print("dist inicial:", dist)

    while pq:
        d, u = heapq.heappop(pq)  # saco el de menor costo
        if vis[u]:                # si ya esta fijo ignoro
            continue
        vis[u] = True             # fijo u
        paso += 1
        print("\npaso", paso, "-> fijo nodo", u, "con costo", d)

        for v, w in adj[u]:       # reviso vecinos
            if vis[v]:
                continue
            nd = d + w            # costo nuevo por u
            print("  veo arista", u, "->", v, "peso", w, "costo nuevo", nd)
            if nd < dist[v]:      # mejora?
                print("   mejora dist de", v, "de", dist[v], "a", nd)
                dist[v] = nd
                heapq.heappush(pq, (nd, v))  # meto candidato
            else:
                print("   no mejora dist de", v, "se queda en", dist[v])

        print("  dist actual:", dist)

    print("\nfin")
    return dist

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
    dist = dijkstra_paso_a_paso(adj, origen)
    print("\nresultado final distancias:", dist)

if __name__ == "__main__":
    demo()
