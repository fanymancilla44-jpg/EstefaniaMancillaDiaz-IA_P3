# dijkstra bidireccional O de E log V
# que hace
#  busca el camino mas corto entre origen y destino usando dos frentes
# por que usarlo
#  en grafos grandes reduce mucho el trabajo si solo te importa un destino
# requisitos
#  pesos no negativos
# representacion
#  grafo no dirigido con lista de adyacencia vecino y peso

import heapq

INF = 10**9

def dijkstra_bidireccional(adj, origen, destino):
    n = len(adj)                 # numero de nodos

    # distancias hacia adelante y hacia atras
    dist_f = [INF] * n
    dist_b = [INF] * n
    dist_f[origen] = 0
    dist_b[destino] = 0

    # padres para reconstruir ruta
    padre_f = [-1] * n
    padre_b = [-1] * n

    # colas de prioridad para ambos lados
    pq_f = [(0, origen)]
    pq_b = [(0, destino)]

    # visitados de cada lado
    vis_f = [False] * n
    vis_b = [False] * n

    # mejor respuesta conocida
    mejor = INF
    meeting = -1                 # donde se encuentran los frentes

    while pq_f or pq_b:
        # paso hacia adelante
        if pq_f:
            df, u = heapq.heappop(pq_f)
            if vis_f[u]:
                pass
            else:
                vis_f[u] = True
                # si este nodo ya fue visto desde atras puedo mejorar mejor
                if vis_b[u]:
                    if dist_f[u] + dist_b[u] < mejor:
                        mejor = dist_f[u] + dist_b[u]
                        meeting = u
                # relajo aristas u -> v
                for v, w in adj[u]:
                    if dist_f[u] + w < dist_f[v]:
                        dist_f[v] = dist_f[u] + w
                        padre_f[v] = u
                        heapq.heappush(pq_f, (dist_f[v], v))

        # paso hacia atras
        if pq_b:
            db, u = heapq.heappop(pq_b)
            if vis_b[u]:
                pass
            else:
                vis_b[u] = True
                # si este nodo ya fue visto desde adelante puedo mejorar mejor
                if vis_f[u]:
                    if dist_f[u] + dist_b[u] < mejor:
                        mejor = dist_f[u] + dist_b[u]
                        meeting = u
                # relajo aristas en sentido inverso que es igual por ser no dirigido
                for v, w in adj[u]:
                    if dist_b[u] + w < dist_b[v]:
                        dist_b[v] = dist_b[u] + w
                        padre_b[v] = u
                        heapq.heappush(pq_b, (dist_b[v], v))

        # condicion de parada temprana
        # si la suma de los minimos al frente no puede superar mejor entonces termino
        top_f = pq_f[0][0] if pq_f else INF
        top_b = pq_b[0][0] if pq_b else INF
        if top_f + top_b >= mejor:
            break

    if mejor == INF:
        return mejor, []         # no hay camino

    # reconstruyo ruta desde origen a meeting y de meeting a destino
    ruta_izq = []
    x = meeting
    while x != -1:
        ruta_izq.append(x)
        x = padre_f[x]
    ruta_izq.reverse()

    ruta_der = []
    x = padre_b[meeting]
    while x != -1:
        ruta_der.append(x)
        x = padre_b[x]

    ruta = ruta_izq + ruta_der
    return mejor, ruta

def demo():
    # grafo no dirigido
    # 0-1 4  0-2 1  2-1 2  1-3 1  2-3 5
    adj = [
        [(1,4),(2,1)],          # 0
        [(0,4),(2,2),(3,1)],    # 1
        [(0,1),(1,2),(3,5)],    # 2
        [(1,1),(2,5)],          # 3
    ]
    origen = 0
    destino = 3
    costo, ruta = dijkstra_bidireccional(adj, origen, destino)
    print("costo:", costo)
    print("ruta :", ruta)

if __name__ == "__main__":
    demo()
