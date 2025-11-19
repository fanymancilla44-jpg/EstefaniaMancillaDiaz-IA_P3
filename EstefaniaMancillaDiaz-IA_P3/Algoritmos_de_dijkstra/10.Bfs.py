# 0 1 bfs para pesos 0 y 1 O de V mas E
# que hace
#  calcula costos minimos cuando cada arista pesa cero o uno
# por que usarlo
#  es mas rapido que dijkstra normal en este caso porque usa deque
#  si el peso es cero meto el vecino al frente
#  si el peso es uno meto el vecino al final

from collections import deque  # deque permite push al frente y al final

INF = 10**9  # infinito practico

def cero_uno_bfs(adj, origen):
    n = len(adj)               # numero de nodos
    dist = [INF] * n           # distancias
    dist[origen] = 0           # origen en cero
    dq = deque([origen])       # deque con el origen

    while dq:
        u = dq.popleft()       # saco por el frente
        for v, w in adj[u]:    # recorro vecinos
            # w debe ser cero o uno
            nd = dist[u] + w   # costo nuevo
            if nd < dist[v]:   # mejora
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)  # peso cero va al frente
                else:
                    dq.append(v)      # peso uno va al final
    return dist

def demo():
    # grafo no dirigido con pesos cero o uno
    # 0-1:1  0-2:0  2-1:0  1-3:1  2-3:1
    adj = [
        [(1,1),(2,0)],        # 0
        [(0,1),(2,0),(3,1)],  # 1
        [(0,0),(1,0),(3,1)],  # 2
        [(1,1),(2,1)],        # 3
    ]
    origen = 0
    dist = cero_uno_bfs(adj, origen)
    print("distancias desde", origen, ":", dist)

if __name__ == "__main__":
    demo()