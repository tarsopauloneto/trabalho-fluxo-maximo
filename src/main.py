import sys
from collections import deque

class Edge:
    """
    Representa uma aresta direcionada na rede de fluxo residual.
    """
    def __init__(self, u, v, capacity):
        self.u = u                  # Vértice de origem
        self.v = v                  # Vértice de destino
        self.capacity = capacity    # Capacidade máxima original da aresta
        self.flow = 0               # Fluxo atual passando pela aresta
        self.reverse = None         # Referência para a aresta de retorno (reversa)

    def residual_capacity(self):
        """Retorna a capacidade residual disponível nesta direção."""
        return self.capacity - self.flow

    def augment(self, delta):
        """Atualiza o fluxo na aresta e o fluxo reverso na aresta oposta."""
        self.flow += delta
        self.reverse.flow -= delta


def bfs(graph, source, sink, parent_edges):
    """
    Busca em Largura (BFS) para encontrar o caminho aumentante mais curto
    em termos de número de arestas (Estratégia do Edmonds-Karp).
    """
    n = len(graph)
    # Inicializa o vetor de pais como None para rastrear o caminho
    for i in range(n):
        parent_edges[i] = None
        
    queue = deque([source])
    visited = [False] * n
    visited[source] = True
    
    while queue:
        curr = queue.popleft()
        
        if curr == sink:
            return True
            
        for edge in graph[curr]:
            # Se o vizinho não foi visitado e a aresta ainda tem capacidade residual
            if not visited[edge.v] and edge.residual_capacity() > 0:
                visited[edge.v] = True
                parent_edges[edge.v] = edge
                queue.append(edge.v)
                
    return visited[sink]


def edmonds_karp(graph, source, sink):
    """
    Executa o método de Ford-Fulkerson utilizando a estratégia de Edmonds-Karp.
    """
    max_flow = 0
    n = len(graph)
    parent_edges = [None] * n
    
    # Enquanto existir um caminho aumentante viável da origem ao sorvedouro
    while bfs(graph, source, sink, parent_edges):
        # 1. Encontra o gargalo (menor capacidade residual) ao longo do caminho encontrado
        bottleneck = float('inf')
        curr = sink
        while curr != source:
            edge = parent_edges[curr]
            bottleneck = min(bottleneck, edge.residual_capacity())
            curr = edge.u
            
        # 2. Aplica o aumento de fluxo ao longo do caminho
        curr = sink
        while curr != source:
            edge = parent_edges[curr]
            edge.augment(bottleneck)
            curr = edge.u
            
        # 3. Acumula o gargalo no fluxo máximo total
        max_flow += bottleneck
        
    return max_flow


def main():
    # Lê toda a entrada da janela padrão de forma otimizada para juízes online
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    network_id = 1
    
    while True:
        try:
            n_str = next(iterator)
        except StopIteration:
            break
            
        n = int(n_str)
        if n == 0:
            break  # Condição de parada do UVA 820
            
        s = int(next(iterator)) - 1  # Convertendo para indexação 0
        t = int(next(iterator)) - 1  # Convertendo para indexação 0
        c = int(next(iterator))
        
        # Matriz de adjacência auxiliar para consolidar arestas paralelas
        adj_matrix = [[0] * n for _ in range(n)]
        
        for _ in range(c):
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            w = int(next(iterator))
            
            if u != v:  # Desconsidera self-loops se houver
                adj_matrix[u][v] += w
                adj_matrix[v][u] += w
        
        # Construção da lista de adjacências com objetos Edge residuais
        graph = [[] for _ in range(n)]
        
        for u in range(n):
            for v in range(u + 1, n):
                cap = adj_matrix[u][v]
                if cap > 0:
                    # Cria as arestas direcionadas correspondentes ao cabo bidirecional
                    e1 = Edge(u, v, cap)
                    e2 = Edge(v, u, cap)
                    
                    # Vincula uma como reversa da outra
                    e1.reverse = e2
                    e2.reverse = e1
                    
                    graph[u].append(e1)
                    graph[v].append(e2)
        
        # Calcula o fluxo máximo usando Edmonds-Karp
        flow = edmonds_karp(graph, s, t)
        
        # Formatação de saída exigida pelo problema
        print(f"Network {network_id}")
        print(f"The bandwidth is {flow}.\n")
        network_id += 1


if __name__ == '__main__':
    main()