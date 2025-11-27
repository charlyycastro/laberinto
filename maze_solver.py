import collections

# --- Algoritmo de Búsqueda en Amplitud (BFS) ---

def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Amplitud (BFS).
    
    Args:
        maze (list of list of int): La matriz del laberinto (0: camino libre, 1: muro).
        start (tuple): Coordenadas de inicio (fila, columna).
        end (tuple): Coordenadas de fin (fila, columna).

    Returns:
        list of tuple or None: La ruta más corta como una lista de coordenadas, o None si no hay camino.
    """
    rows, cols = len(maze), len(maze[0])
    # Cola para BFS: almacena ((fila, columna), [camino hasta aquí])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: derecha, izquierda, abajo, arriba (dr, dc)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            # Verificar límites y si es camino libre (0) y no ha sido visitado
            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                
                visited.add((next_row, next_col))
                # Crear una nueva lista para el camino
                new_path = list(path) 
                new_path.append((next_row, next_col))
                queue.append(((next_row, next_col), new_path))
    
    return None # No se encontró camino

# --- Representación del Laberinto ---
# (0: camino libre, 1: muro)

MAZE = [
        [0,1,0,0,0,0,1,0,0,0],
        [0,1,0,1,1,0,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [1,1,1,0,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,0,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [0,1,1,0,0,0,1,0,0,0]
    ]

START = (0, 0) # Fila 0, Columna 0
END = (9, 9)   # Fila 9, Columna 9