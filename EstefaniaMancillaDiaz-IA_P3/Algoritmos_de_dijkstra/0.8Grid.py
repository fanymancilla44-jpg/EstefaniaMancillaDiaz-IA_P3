# dijkstra en grid con 4 u 8 direcciones
# que hace
#  busca el camino mas corto en una cuadricula con celdas libres y muros
# para que sirve
#  mapas tipo laberinto o tableros donde cada paso cuesta lo mismo
# representacion
#  grid como lista de cadenas con caracteres
#  . celda libre
#  # muro
#  s inicio
#  g meta

import heapq  # cola de prioridad binaria

INF = 10**9  # infinito practico

def vecinos_de(r, c, R, C, diagonales):
    # genera vecinos validos segun 4 o 8 direcciones
    dirs4 = [(-1,0),(1,0),(0,-1),(0,1)]
    dirs8 = dirs4 + [(-1,-1),(-1,1),(1,-1),(1,1)]
    for dr, dc in (dirs8 if diagonales else dirs4):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            costo = 14 if diagonales and dr != 0 and dc != 0 else 10  # diag vale 1 punto 4 aprox
            yield nr, nc, costo

def dijkstra_grid(grid, diagonales=False):
    # ubicamos inicio y meta
    R = len(grid)
    C = len(grid[0])
    ini = meta = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                ini = (r, c)
            elif grid[r][c] == "G":
                meta = (r, c)
    if ini is None or meta is None:
        raise ValueError("faltan S o G en el grid")

    # distancias y padres
    dist = [[INF]*C for _ in range(R)]
    padre = [[None]*C for _ in range(R)]
    ir, ic = ini
    dist[ir][ic] = 0

    # cola de prioridad con tupla costo y posicion
    pq = [(0, ir, ic)]

    while pq:
        d, r, c = heapq.heappop(pq)
        # si este par esta viejo lo brinco
        if d != dist[r][c]:
            continue
        # parada temprana si llegamos a la meta
        if (r, c) == meta:
            break
        # si es muro no expandimos
        if grid[r][c] == "#":
            continue
        # relajo vecinos validos que no sean muro
        for nr, nc, w in vecinos_de(r, c, R, C, diagonales):
            if grid[nr][nc] == "#":
                continue
            nd = d + w
            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                padre[nr][nc] = (r, c)
                heapq.heappush(pq, (nd, nr, nc))

    return dist, padre, ini, meta

def reconstruir_ruta(padre, ini, meta):
    # arma ruta desde meta hasta ini usando padre
    r, c = meta
    ruta = []
    while (r, c) is not None:
        ruta.append((r, c))
        if (r, c) == ini:
            break
        p = padre[r][c]
        if p is None:
            return []  # no hay camino
        r, c = p
    ruta.reverse()
    return ruta

def pintar_ruta(grid, ruta):
    # devuelve una version del grid con la ruta marcada con asteriscos
    g2 = [list(fila) for fila in grid]
    for r, c in ruta:
        if g2[r][c] not in ("S","G"):
            g2[r][c] = "*"
    return ["".join(f) for f in g2]

def demo():
    # mapa simple
    # S inicio
    # G meta
    # # muro
    # . libre
    grid = [
        "S..#....",
        ".##.#..G",
        ".#...#..",
        ".#.#....",
        "...#....",
    ]

    # correr con 4 direcciones
    dist4, padre4, ini, meta = dijkstra_grid(grid, diagonales=False)
    ruta4 = reconstruir_ruta(padre4, ini, meta)
    pintado4 = pintar_ruta(grid, ruta4)
    print("grid con 4 direcciones:")
    for fila in pintado4:
        print(fila)
    if ruta4:
        costo4 = dist4[meta[0]][meta[1]] / 10.0
        print("costo 4 dirs:", costo4)
    else:
        print("no hay ruta con 4 direcciones")

    print()

    # correr con 8 direcciones
    dist8, padre8, ini, meta = dijkstra_grid(grid, diagonales=True)
    ruta8 = reconstruir_ruta(padre8, ini, meta)
    pintado8 = pintar_ruta(grid, ruta8)
    print("grid con 8 direcciones:")
    for fila in pintado8:
        print(fila)
    if ruta8:
        costo8 = dist8[meta[0]][meta[1]] / 10.0
        print("costo 8 dirs:", costo8)
    else:
        print("no hay ruta con 8 direcciones")

if __name__ == "__main__":
    demo()