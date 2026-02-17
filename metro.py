from collections import deque

# ============================================================
# Construcción del grafo (Lista de Adyacencia)
# El metro CDMX fue simplificado solo con las lineas necesarias
# ============================================================

def agregar_arista(graph, u, v):
    """Agrega una arista no dirigida"""
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)


def construccion_grafo():
    graph = {}

    linea1 = [
        "Observatorio", "Tacubaya", "Juanacatlan", "Chapultepec",
        "Sevilla", "Insurgentes", "Cuauhtemoc", "Balderas",
        "Salto del Agua", "Isabel la Catolica", "Pino Suarez",
        "Merced", "Candelaria", "San Lazaro", "Moctezuma",
        "Balbuena", "Boulevard Puerto Aereo", "Gomez Farias",
        "Zaragoza", "Pantitlan"
    ]

    linea2 = [
        "Cuatro Caminos", "Panteones", "Tacuba", "Cuitlahuac",
        "Popotla", "Colegio Militar", "Normal", "San Cosme",
        "Revolucion", "Hidalgo", "Bellas Artes", "Allende",
        "Zocalo", "Pino Suarez", "San Antonio Abad",
        "Chabacano", "Viaducto", "Xola", "Villa de Cortes",
        "Nativitas", "Portales", "Ermita", "General Anaya",
        "Tasqueña"
    ]

    linea3 = [
        "Indios Verdes", "Deportivo 18 de Marzo", "Potrero",
        "La Raza", "Tlatelolco", "Guerrero", "Hidalgo",
        "Juarez", "Balderas", "Ninos Heroes",
        "Hospital General", "Centro Medico", "Etiopia",
        "Eugenia", "Division del Norte", "Zapata",
        "Coyoacan", "Viveros", "Miguel Angel de Quevedo",
        "Copilco", "Universidad"
    ]

    linea4 = [
        "Martin Carrera", "Talisman", "Bondojito",
        "Consulado", "Canal del Norte", "Morelos",
        "Candelaria", "Fray Servando",
        "Jamaica", "Santa Anita"
    ]

    linea5 = [
        "Politecnico", "Instituto del Petroleo",
        "Autobuses del Norte", "La Raza",
        "Misterios", "Valle Gomez",
        "Consulado", "Eduardo Molina",
        "Aragon", "Oceanía",
        "Terminal Aerea", "Hangares",
        "Pantitlan"
    ]

    linea6 = [
        "El Rosario", "Tezozomoc", "Azcapotzalco",
        "Ferreria", "Norte 45",
        "Vallejo", "Instituto del Petroleo",
        "Lindavista", "Deportivo 18 de Marzo",
        "Martin Carrera"
    ]

    linea7 = [
        "El Rosario", "Aquiles Serdan",
        "Camarones", "Refineria",
        "Tacuba", "San Joaquin",
        "Polanco", "Auditorio",
        "Constituyentes", "Tacubaya",
        "San Pedro de los Pinos",
        "San Antonio", "Mixcoac",
        "Barranca del Muerto"
    ]

    linea8 = [
        "Garibaldi", "Bellas Artes",
        "San Juan de Letran",
        "Salto del Agua",
        "Doctores", "Obrera",
        "Chabacano", "La Viga",
        "Santa Anita", "Coyuya",
        "Iztacalco", "Apatlaco",
        "Aculco", "Escuadron 201",
        "Atlalilco", "Iztapalapa",
        "Cerro de la Estrella",
        "UAM-I", "Constitucion de 1917"
    ]

    linea9 = [
        "Tacubaya", "Patriotismo",
        "Chilpancingo", "Centro Medico",
        "Lazaro Cardenas", "Chabacano",
        "Jamaica", "Mixiuhca",
        "Velodromo", "Ciudad Deportiva",
        "Puebla", "Pantitlan"
    ]

    lineaA = [
        "Pantitlan", "Agricola Oriental",
        "Canal de San Juan",
        "Tepalcates", "Guelatao",
        "Penon Viejo", "Acatitla",
        "Santa Marta",
        "Los Reyes", "La Paz"
    ]

    lineaB = [
        "Buenavista", "Guerrero",
        "Garibaldi", "Lagunilla",
        "Tepito", "Morelos",
        "San Lazaro", "Ricardo Flores Magon",
        "Romero Rubio", "Oceanía",
        "Deportivo Oceanía",
        "Bosque de Aragon",
        "Villa de Aragon",
        "Nezahualcoyotl",
        "Impulsora",
        "Rio de los Remedios",
        "Muzquiz",
        "Ecatepec",
        "Olimpica",
        "Plaza Aragon",
        "Ciudad Azteca"
    ]

    # Función para conectar estaciones consecutivas
    def coneccion_linea(line):
        for i in range(len(line) - 1):
            agregar_arista(graph, line[i], line[i + 1])

    for linea in [linea1, linea2, linea3, linea4, linea5,
                  linea6, linea7, linea8, linea9,
                  lineaA, lineaB]:
        coneccion_linea(linea)

    return graph


# ============================================================
# BFS
# ============================================================

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if goal not in parent:
        return None, 0, nodes_expanded

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, len(path) - 1, nodes_expanded


# ============================================================
# DFS
# ============================================================

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}
    nodes_expanded = 0

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal:
                break

            for neighbor in graph[current]:
                if neighbor not in visited:
                    parent[neighbor] = current
                    stack.append(neighbor)

    if goal not in parent:
        return None, 0, nodes_expanded

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path, len(path) - 1, nodes_expanded


# ============================================================
# Ejecución de casos obligatorios
# ============================================================

def ejecutar_caso(graph, start, goal):
    print("=================================================")
    print(f"Caso: {start} -> {goal}\n")

    print("BFS:")
    path, jumps, visited = bfs(graph, start, goal)
    print("Ruta encontrada:", path)
    print("Longitud en aristas:", jumps)
    print("Nodos visitados:", visited)
    print()

    print("DFS:")
    path, jumps, visited = dfs(graph, start, goal)
    print("Ruta encontrada:", path)
    print("Longitud en aristas:", jumps)
    print("Nodos visitados:", visited)
    print()


if __name__ == "__main__":
    graph = construccion_grafo()

    # Casos obligatorios
    ejecutar_caso(graph, "Observatorio", "Ciudad Azteca")
    ejecutar_caso(graph, "Indios Verdes", "Velodromo")
    ejecutar_caso(graph, "UAM-I", "El Rosario")
