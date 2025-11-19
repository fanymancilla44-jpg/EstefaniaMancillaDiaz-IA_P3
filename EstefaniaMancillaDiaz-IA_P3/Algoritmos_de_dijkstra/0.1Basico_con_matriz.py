# dijkstra basico con matriz O de V cuadrada
# que hace
#  calcula el costo minimo desde un nodo origen a todos los demas
#  solo funciona si todos los pesos son no negativos
# para que sirve
#  sirve para rutas mas cortas cuando el grafo no es gigante


INF = 10**9  # inf es un numero muy grande para simular infinito en distancias

def dijkstra_matriz(mat, origen):  # def define una funcion con nombre y parametros
    n = len(mat)  # n guarda el numero de nodos usando la longitud de la matriz
    dist = [INF] * n  # dist es una lista con n copias de inf para iniciar todas las distancias
    dist[origen] = 0  # al origen le ponemos distancia cero porque es el punto de arranque
    vis = [False] * n  # vis es una lista de booleanos para saber si ya fijamos un nodo

    for _ in range(n):  # ciclo que se repite a lo sumo n veces una por nodo
        u = -1  # u guardara el indice del nodo elegido en esta vuelta
        mejor = INF  # mejor guarda la menor distancia encontrada hasta ahora en esta vuelta

        for i in range(n):  # recorro todos los nodos para buscar el no visitado mas barato
            if not vis[i] and dist[i] < mejor:  # si no esta visitado y su distancia es menor actualizo el candidato
                mejor = dist[i]  # guardo la nueva mejor distancia
                u = i  # guardo el indice del nodo candidato

        if u == -1:  # si u queda en menos uno significa que no hay nodos alcanzables restantes
            break  # salgo del ciclo principal porque ya no hay nada que mejorar

        vis[u] = True  # marco el nodo u como visitado para no procesarlo otra vez

        for v in range(n):  # ahora recorro posibles vecinos v del nodo u
            w = mat[u][v]  # w es el peso de la arista de u a v tomado de la matriz
            if w > 0 and not vis[v]:  # si hay arista y v no esta visitado entonces puedo intentar mejorar
                if dist[u] + w < dist[v]:  # si el camino pasando por u da menor distancia entonces actualizo
                    dist[v] = dist[u] + w  # guardo la nueva distancia mas corta hacia v

    return dist  # regreso la lista de distancias finales desde el origen

def demo():  # funcion demo para correr un ejemplo rapido
    # nodos 0 1 2 3
    # 0 a 1 costo 4
    # 0 a 2 costo 1
    # 2 a 1 costo 2
    # 1 a 3 costo 1
    # 2 a 3 costo 5
    mat = [  # defino la matriz de pesos del grafo de ejemplo
        [0, 4, 1, 0],
        [4, 0, 2, 1],
        [1, 2, 0, 5],
        [0, 1, 5, 0],
    ]
    origen = 0  # defino el nodo de inicio para el algoritmo
    dist = dijkstra_matriz(mat, origen)  # llamo a la funcion para calcular distancias
    print("distancias desde", origen, ":", dist)  # imprimo la lista resultante de distancias

if __name__ == "__main__":  # este bloque se ejecuta solo si corro el archivo directo
    demo()  # llamo a la demo para ver el resultado en consola