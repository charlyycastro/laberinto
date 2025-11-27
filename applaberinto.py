import streamlit as st
import pandas as pd
# Importar las variables y la función de resolución desde maze_solver
from maze_solver import MAZE, START, END, solve_maze_bfs

st.set_page_config(layout="wide")
st.title("Visualizador de Algoritmo de Búsqueda en Laberinto (BFS)")

# --- Función para renderizar el laberinto ---
def render_maze(maze, path=None):
    """Renderiza el laberinto usando emojis en Streamlit."""
    if path is None:
        path = []
    
    # Convertir la lista de tuplas del camino a un set para búsqueda rápida
    path_set = set(path)
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            current_pos = (r_idx, c_idx)
            
            if current_pos == START:
                display_row.append("🚀") # Inicio
            elif current_pos == END:
                display_row.append("🏁") # Fin
            elif current_pos in path_set:
                # Usar un emoji para el camino resuelto, excluyendo Inicio y Fin ya marcados
                display_row.append("🔹") 
            elif col == 1:
                display_row.append("⬛") # Muro
            else:
                display_row.append("⬜") # Camino libre
        
        # Añadir un espacio entre emojis para una mejor visualización en Streamlit
        display_maze.append(" ".join(display_row))
    
    # Usar st.markdown para renderizar el laberinto como texto formateado
    st.markdown("### Laberinto")
    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)
    
    # Agregar nota sobre la leyenda
    st.caption("Leyenda: 🚀=Inicio, 🏁=Fin, ⬛=Muro, ⬜=Camino Libre, 🔹=Ruta Encontrada")


# --- Sidebar y Controles ---
st.sidebar.header("Opciones de Resolución")
algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo", 
    ["BFS (Implementado)", "DFS (No implementado)", "A* (No implementado)"]
)
solve_button = st.sidebar.button("Resolver Laberinto")

# Mostrar el laberinto inicial (o el resuelto si se presionó el botón)
if solve_button:
    if algorithm == "BFS (Implementado)":
        # Ejecutar el algoritmo BFS
        path = solve_maze_bfs(MAZE, START, END)
        
        if path:
            st.success(f"✅ ¡Camino encontrado con {algorithm}!")
            # Renderizar el laberinto con el camino encontrado
            render_maze(MAZE, path)
            st.markdown(f"**Longitud del camino:** {len(path)} pasos.")
            st.markdown(f"**Coordenadas del camino:** {path}")
            # 
        else:
            st.error("❌ No se encontró un camino para este laberinto con el algoritmo BFS.")
            render_maze(MAZE) # Mostrar el laberinto sin resolver
    else:
        st.warning(f"⚠️ El algoritmo {algorithm} aún no está implementado.")
        render_maze(MAZE) # Mostrar el laberinto sin resolver
else:
    # Mostrar el laberinto sin resolver por defecto
    render_maze(MAZE)