import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(archivo):
    """
    Lee el archivo de gramática y devuelve las componentes de la gramática: V_nt, V_i, S, P, cadena.
    """
    with open(archivo, 'r') as f:
        gramatica = f.readlines()

    componentes = {
        "V_nt": [],  # Variables no terminales
        "V_i": [],   # Variables terminales
        "S": None,   # Símbolo inicial
        "P": [],     # Producciones
        "cadena": [] # Cadena a derivar
    }

    for linea in gramatica:
        linea = linea.strip()
        if linea.startswith("V_nt:"):
            componentes["V_nt"] = linea.replace("V_nt:", "").strip().split()
        elif linea.startswith("V_i:"):
            componentes["V_i"] = linea.replace("V_i:", "").strip().split()
        elif linea.startswith("S:"):
            componentes["S"] = linea.replace("S:", "").strip()
        elif linea.startswith("P:"):
            continue  # Ignorar la línea que solo contiene 'P:'
        elif linea.startswith("cadena:"):
            componentes["cadena"] = list(linea.replace("cadena:", "").strip())
        else:
            # Procesar producción
            if "->" in linea:
                izquierda, derecha = linea.split("->")
                izquierda = izquierda.strip()
                derecha = derecha.strip().split()  # Separar múltiples símbolos en la parte derecha
                componentes["P"].append((izquierda, derecha))
    
    return componentes

def expandir_gramatica(gramatica, simbolo, G, padre=None):
    """
    Expande un símbolo dado según las producciones de la gramática y añade nodos y aristas al grafo.
    """
    for produccion in gramatica["P"]:
        izq, der = produccion
        if izq == simbolo:
            for simbolo_der in der:
                G.add_node(simbolo_der, label=simbolo_der)
                if padre:
                    G.add_edge(padre, simbolo_der)
                # Si es no terminal, se sigue expandiendo
                if simbolo_der in gramatica["V_nt"]:
                    expandir_gramatica(gramatica, simbolo_der, G, simbolo_der)

def generar_arbol_cadena(gramatica):
    """
    Genera el árbol de derivación basado solo en la cadena dada utilizando las producciones de la gramática.
    """
    G = nx.DiGraph()  # Grafo dirigido para representar el árbol
    
    # Expandir el símbolo inicial
    simbolo_inicial = gramatica["S"]
    
    # Verificar si el símbolo inicial está en las producciones
    if simbolo_inicial not in [prod[0] for prod in gramatica["P"]]:
        print("El símbolo inicial no tiene producción asociada.")
        return G
    
    G.add_node(simbolo_inicial, label=simbolo_inicial)
    
    # Expansión recursiva del símbolo inicial
    expandir_gramatica(gramatica, simbolo_inicial, G, simbolo_inicial)
    
    return G

def visualizar_arbol(G):
    """
    Visualiza el grafo como un árbol utilizando NetworkX y Matplotlib.
    """
    if len(G) == 0:
        print("El grafo no tiene nodos para dibujar.")
        return
    
    pos = nx.spring_layout(G)  # Intentar con un layout diferente
    etiquetas = nx.get_node_attributes(G, 'label')
    
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, labels=etiquetas, with_labels=True, node_color="lightblue", 
            font_size=12, font_weight='bold', node_size=3000, font_color='black', arrows=True)
    plt.title("Árbol derivado de la cadena")
    plt.show()

# Programa principal
def main():
    archivo_gramatica = "Estados.txt"  # Nombre del archivo gramatical
    gramatica = leer_gramatica(archivo_gramatica)
    
    print("Gramática leída:")
    print("No terminales:", gramatica["V_nt"])
    print("Terminales:", gramatica["V_i"])
    print("Símbolo inicial:", gramatica["S"])
    print("Producciones:", gramatica["P"])
    print("Cadena:", gramatica["cadena"])
    
    # Verificar si la cadena tiene símbolos no terminales que no pertenecen a las producciones
    for simbolo in gramatica["cadena"]:
        if simbolo not in gramatica["V_nt"] and simbolo not in gramatica["V_i"]:
            print(f"El símbolo '{simbolo}' en la cadena no está en las producciones ni en las variables.")
            return
    
    # Generar el árbol (grafo dirigido) solo de la cadena
    grafo_arbol = generar_arbol_cadena(gramatica)
    
    # Si el grafo está vacío, no visualizar nada
    if len(grafo_arbol.nodes) == 0:
        print("El grafo está vacío, no hay nada que visualizar.")
    else:
        # Visualizar el árbol
        visualizar_arbol(grafo_arbol)

if __name__ == "__main__":
    main()
