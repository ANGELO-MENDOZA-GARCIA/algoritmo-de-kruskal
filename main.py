# Angelo Mendoza García - 230300813
# Fecha: 3-11-2024

# Fuente Artículo https://www.researchgate.net/publication/320714849_Research_and_Improvement_of_Kruskal_Algorithm

# Importamos la librería pandas para manejar el archivo CSV
import pandas as pd

# Función para leer el archivo CSV y retornar el DataFrame
def read_file(url):
    # Leemos el archivo desde la URL proporcionada y lo almacenamos en un DataFrame
    df = pd.read_csv(url)
    return df

# Función para calcular la cantidad de nodos
def calcular_nodos(df):
    # Verificamos si los nodos son letras
    if isinstance(df['Source'].iloc[0], str):
        # Creamos un mapeo de letras a números
        letras = sorted(set(df['Source']).union(set(df['Destination'])))
        mapeo = {letra: idx for idx, letra in enumerate(letras)}
        # Convertimos las letras a números usando el mapeo
        df['Source'] = df['Source'].map(mapeo)
        df['Destination'] = df['Destination'].map(mapeo)
    
    # Encontramos el nodo máximo entre los valores de las columnas de origen y destino
    max_nodo = max(df['Source'].max(), df['Destination'].max())
    # Sumamos 1 al máximo para obtener la cantidad total de nodos
    return max_nodo + 1

# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

# Class to represent a graph 
class Graph: 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 

    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 

    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 

            # Reassignment of node's parent 
            # to root node as 
            # path compression requires 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 

        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1

    # The main function to construct MST 
    # using Kruskal's algorithm 
    def KruskalMST(self): 

        # This will store the resultant MST 
        result = [] 

        # An index variable, used for sorted edges 
        i = 0

        # An index variable, used for result[] 
        e = 0

        # Sort all the edges in 
        # non-decreasing order of their 
        # weight 
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 

        parent = [] 
        rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        # Number of edges to be taken is less than to V-1 
        while e < self.V - 1: 

            # Pick the smallest edge and increment 
            # the index for next iteration 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            # If including this edge doesn't 
            # cause cycle, then include it in result 
            # and increment the index of result 
            # for next edge 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 

        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            minimumCost += weight 
            print("%d -- %d == %d" % (u, v, weight)) 
        print("Minimum Spanning Tree", minimumCost) 


# Código principal
if __name__ == '__main__': 
    # URLs de los archivos CSV en el repositorio de GitHub
    urls = [
        "https://raw.githubusercontent.com/ANGELO-MENDOZA-GARCIA/algoritmo-de-kruskal/refs/heads/main/grafo_4_nodos.csv",
        "https://raw.githubusercontent.com/ANGELO-MENDOZA-GARCIA/algoritmo-de-kruskal/refs/heads/main/grafo_9_nodos.csv",
        "https://raw.githubusercontent.com/ANGELO-MENDOZA-GARCIA/algoritmo-de-kruskal/refs/heads/main/grafo_articulo.csv"
    ]
    
    for url in urls:
        print(f"Procesando archivo: {url}")
        
        # Leemos el archivo CSV
        df = read_file(url)
        
        # Calculamos la cantidad de nodos
        cant_nodos = calcular_nodos(df)
        
        # Imprimimos la cantidad de nodos
        print("Cantidad de nodos:", cant_nodos)
            
        # Creamos el grafo con la cantidad de nodos calculada
        g = Graph(cant_nodos)
        
        # Obtenemos el número de filas y columnas en el DataFrame
        filas, columnas = df.shape
        
        # Agregamos las aristas al grafo a partir del DataFrame
        for i in range(filas):
            # Extraemos el nodo origen, nodo destino y peso desde el DataFrame
            u = df.iloc[i, 1]  # Columna de origen
            v = df.iloc[i, 2]  # Columna de destino
            w = df.iloc[i, 0]  # Columna de peso
            g.addEdge(u, v, w)
        
        # Llamamos al algoritmo de Kruskal para obtener el árbol de expansión mínima
        g.KruskalMST()
        print("\n")
