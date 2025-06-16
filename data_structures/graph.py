import random
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import networkx as nx


class Graph(ABC):
    """ Abstract class for computational graphs.
    """
    def __init__(self, graph: list[any] = []):
        self.num_nodes = 0
        self.num_edges = 0
        self.graph = graph
        self.net_graph = None
    
    @abstractmethod
    def rand_create(num_nodes: int, num_edges: int):
        pass

    @abstractmethod
    def plot_graph(self):
        pass

    def _draw_netx_graph(self):
        # Draw the graph
        pos = nx.spring_layout(self.net_graph)
        nx.draw(self.net_graph, pos, with_labels=True, node_color='skyblue', node_size=1000, arrows=True)

        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(self.net_graph, 'weight')
        nx.draw_networkx_edge_labels(self.net_graph, pos, edge_labels=edge_labels)
        
        plt.show()


class GridMatrix(Graph):
    pass


class AdjacencyMatrix(Graph):
    pass

    def rand_create(self, num_nodes: int, num_edges: int):
        """ Randomly creates an NxN adjacency matrix (N =: num_nodes) with M (num_edges) edges.
        This will be a directed, unweighted graph that allows self-loop.
        """
        self.graph = [[0] * num_nodes for _ in range(num_nodes)]
        graph_coords = [(r, c) for r in range(num_nodes) for c in range(num_nodes)]
        edge_coords = random.sample(graph_coords, k=num_edges)
        for r, c in edge_coords:
            self.graph[r][c] = 1

    def plot_graph(self):
        if not self.net_graph:
            # Initialise directed graph with nodes
            self.net_graph = nx.DiGraph()
            for i in range(len(self.graph)):
                self.net_graph.add_node(i)

            # Iterate through matrix & add all edges
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    if self.graph[i][j] != 0:
                        self.net_graph.add_edge(i, j, weight=self.graph[i][j])
                    if self.graph[j][i] != 0:
                        self.net_graph.add_edge(j, i, weight=self.graph[j][i])

        self._draw_netx_graph()


class AdjacencyList(Graph):
    pass


class EdgeList(Graph):
    pass


if __name__ == '__main__':
    graph = AdjacencyMatrix()
    graph.rand_create(5, 6)
    graph.plot_graph()
