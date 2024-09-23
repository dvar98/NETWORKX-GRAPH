# Generador de Árbol de Derivación para Gramáticas

Este proyecto genera un árbol de derivación basado en una gramática libre de contexto proporcionada en un archivo de texto. El árbol se genera a partir de las reglas de producción de la gramática y la cadena inicial, y se visualiza utilizando las librerías **NetworkX** y **Matplotlib**.

## Requisitos

Este proyecto requiere Python 3.x y las siguientes librerías:

- `networkx`
- `matplotlib`

Puedes instalar estas dependencias utilizando el siguiente comando:

```bash
pip install networkx matplotlib
```

## Estructura de la Gramática

El archivo de gramática debe estar formateado de la siguiente manera:
```
V_nt: S A B            # Variables no terminales
V_i: a b               # Variables terminales
S: S                   # Símbolo inicial
P:                     # Reglas de producción
S -> A B
A -> a
B -> b
cadena: S              # Cadena a derivar
```

* V_nt: Lista de variables no terminales, separadas por espacios.
* V_i: Lista de variables terminales, separadas por espacios.
* S: El símbolo inicial de la gramática.
* P: Reglas de producción en el formato X -> Y1 Y2 ... Yn.
* cadena: Cadena que se va a derivar a partir de las producciones.

## Funcionamiento del Código

El programa primero lee el archivo de gramática utilizando la función leer_gramatica.
Después, se genera un árbol de derivación a partir del símbolo inicial y las reglas de producción.
Finalmente, el árbol se visualiza como un grafo dirigido utilizando NetworkX y Matplotlib.

## Flujo del Programa

Leer la gramática: La gramática es leída desde un archivo, identificando las variables no terminales, terminales, el símbolo inicial y las producciones.
Generar el árbol de derivación: El árbol se genera comenzando desde el símbolo inicial, expandiendo cada símbolo no terminal de acuerdo a las reglas de producción.
Visualización: El árbol se visualiza en un gráfico utilizando Matplotlib.

##Uso

Modifica el archivo Estados.txt o crea uno propio con el formato adecuado.
Ejecuta el programa principal.
```
python main.py
```
## Ejemplo

Para la siguiente gramática en Estados.txt:

```
V_nt: S A B
V_i: a b
S: S
P:
S -> A B
A -> a
B -> b
cadena: S
```

El programa generará un árbol de derivación con el siguiente formato:

    Nodo raíz: S
    Producciones:
        S -> A B
        A -> a
        B -> b

El grafo visualizado mostrará las conexiones entre los símbolos según las producciones.
Manejo de Errores

    Si la cadena contiene símbolos que no están definidos en la gramática, el programa devolverá un mensaje de error y no generará el árbol.
    Si no hay producciones para expandir el símbolo inicial, se informará que no hay aristas para visualizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.


## Integrantes 

- Daniel Santiago Varela Guerrero
- Miguel Angel Velasco
- Sebastian Sabogal Castillo
