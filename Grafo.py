import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica_y_cadena(archivo):
    """
    Lee la gramática y la cadena desde un archivo de texto.

    Args:
        archivo (str): Nombre del archivo con la gramática.

    Returns:
        tuple: Diccionario con las componentes de la gramática y la cadena.
    """
    with open(archivo, 'r') as f:
        gramatica = f.readlines()

    componentes = {
        "V_nt": [],
        "V_i": [],
        "S": None,
        "P": [],
        "cadena": ""
    }

    leyendo_producciones = False
    for linea in gramatica:
        linea = linea.strip()
        if linea.startswith("V_nt:"):
            componentes["V_nt"] = linea.replace("V_nt:", "").strip().split()
        elif linea.startswith("V_i:"):
            componentes["V_i"] = linea.replace("V_i:", "").strip().split()
        elif linea.startswith("S:"):
            componentes["S"] = linea.replace("S:", "").strip()
        elif linea.startswith("P:"):
            leyendo_producciones = True
            continue
        elif "cadena:" in linea:
            componentes["cadena"] = linea.replace("cadena:", "").strip()
        elif leyendo_producciones:
            if "->" in linea:
                izquierda, derecha = linea.split("->")
                izquierda = izquierda.strip()
                derecha = derecha.strip().split()
                componentes["P"].append((izquierda, derecha))
    
    return componentes


def generar_grafo_cadena(gramatica):
    """
    Crea un grafo dirigido que sigue el derivado de la cadena con la gramática.

    Args:
        gramatica (dict): Diccionario con las componentes de la gramática.

    Returns:
        nx.DiGraph: Grafo dirigido representando la derivación de la cadena.
    """
    G = nx.DiGraph()
    cadena_a_generar = list(gramatica["cadena"])
    
    # Punto de partida
    apuntador = gramatica["S"]

    # Paso de derivación
    derivacion = [apuntador]
    G.add_node(apuntador, tipo="no_terminal")

    while derivacion:
        parte_actual = derivacion.pop(0)

        for produccion in gramatica["P"]:
            if parte_actual == produccion[0] and produccion[1] == cadena_a_generar[:len(produccion[1])]:
                # Añadir la transición al grafo
                for simbolo in produccion[1]:
                    G.add_edge(parte_actual, simbolo)
                    derivacion.append(simbolo)
                    parte_actual = simbolo
                cadena_a_generar = cadena_a_generar[len(produccion[1]):]
                break

    return G

def visualizar_grafo(G):
    """
    Visualiza el grafo utilizando Matplotlib.

    Args:
        G (nx.DiGraph): Grafo dirigido.
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_size=10, node_size=3000, font_color="black", font_weight='bold', arrows=True)
    plt.show()

def main():
    archivo_gramatica = "Estados.txt"
    gramatica = leer_gramatica_y_cadena(archivo_gramatica)
    grafo = generar_grafo_cadena(gramatica)
    visualizar_grafo(grafo)

if __name__ == "__main__":
    main()

