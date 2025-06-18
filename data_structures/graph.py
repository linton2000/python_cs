from random import random, sample
from abc import ABC, abstractmethod
from math import ceil, sqrt

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import ListedColormap


class Graph(ABC):
    """ Abstract class for computational graphs.
    """
    def __init__(self, graph: list[any] = []):
        self.num_nodes = 0
        self.num_edges = 0
        self.graph = graph
        self.net_graph = None
    
    @abstractmethod
    def rand_create(self, num_nodes: int, num_edges: int):
        pass

    @abstractmethod
    def plot_graph(self):
        pass

    def _draw_netx_graph(self):
        """ Helper to plot graph using `networkx` library calls.
        """
        # Draw the graph
        pos = nx.spring_layout(self.net_graph)
        nx.draw(self.net_graph, pos, with_labels=True, node_color='skyblue', node_size=1000, arrows=True)

        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(self.net_graph, 'weight')
        nx.draw_networkx_edge_labels(self.net_graph, pos, edge_labels=edge_labels)
        
        plt.show()


class GridMatrix(Graph):
    """ 2D Grid Matrix implementation of an undirected, unweighted graph with no self-loops, i.e. a maze.
    """
    def __init__(self, graph = []):
        super().__init__(graph)
    
    def rand_create(self, num_nodes, num_edges=None, has_path=True):
        """ Randomly create a 2D grid graph with N (`num_nodes`) nodes. Ignoring `num_edges` because the
        no. of edges is fully dependent on N. Also has a `has_path` param to carve a path from top left
        to bottom right if needed.

        0 - A node with undirected, weighted edges to nearby (up/down/left/right) neighbour nodes.
        1 - A blocked path (eg. wall in a maze).
        """
        if has_path:
            self.graph = self._make_graph_with_path(num_nodes)
        else:
            side = ceil(sqrt(num_nodes)) + 2  # Create a generous grid
            graph = [[1] * side for _ in range(side)]

            # Flatten list of all coordinates
            all_cells = [(i, j) for i in range(side) for j in range(side)]

            # Randomly sample num_nodes cells to set to 0
            node_cells = sample(all_cells, num_nodes)

            for i, j in node_cells:
                graph[i][j] = 0

            self.graph = graph
        
        self.num_nodes = num_nodes
        self.num_edges = self._count_edges()

    def plot_graph(self):
        maze = np.array(self.graph, dtype=int)
        cmap = ListedColormap(['white', 'black'])  # 0=white, 1=black explicitly
        
        plt.figure(figsize=(6,6))
        plt.imshow(maze, cmap=cmap, origin='upper')
        plt.xticks([])
        plt.yticks([])
        plt.show()

    def _count_edges(self):
        rows = len(self.graph)
        cols = len(self.graph[0]) if rows > 0 else 0
        edges = 0

        for i in range(rows):
            for j in range(cols):
                if self.graph[i][j] == 0:
                    # Only check right and down to avoid double-counting
                    if j + 1 < cols and self.graph[i][j + 1] == 0:  # Check right
                        edges += 1
                    if i + 1 < rows and self.graph[i + 1][j] == 0:  # Check down
                        edges += 1

        return edges

    def _make_graph_with_path(self, num_nodes):
        side = ceil(sqrt(num_nodes)) + 2  # To create a big enough grid
        graph = [[1] * side for _ in range(side)]

        # Create random path from top left to bottom right
        x, y = 0, 0
        path = [(0, 0)]
        while x < side - 1 or y < side - 1:
            if x == side - 1:
                y += 1
            elif y == side - 1:
                x += 1
            else:
                if random() < 0.5:
                    x += 1
                else:
                    y += 1
            path.append((x, y))
        
        # Carve out this path in matrix
        for i, j in path:
            graph[i][j] = 0

        # Fill out the rest of the grid to satisfy num_nodes
        remaining_zeros = num_nodes - len(path)
        if remaining_zeros < 0:
            raise ValueError(f"`num_nodes` is too small to fit even the minimal path. \
                             Need {side ** 2} nodes to guarantee successful random GridMatrix creation with path.")
        non_path_coords = [(x, y) for x in range(side) for y in range(side) if graph[x][y] == 1]
        i = 0
        while remaining_zeros > 0:
            x, y = non_path_coords[i]
            graph[x][y] = 0
            remaining_zeros -= 1
            i += 1
        
        return graph
        

class AdjacencyMatrix(Graph):
    """ Adjacency Matrix implementation of the Graph interface. Graphs are directed & unweighted with self-loops.
    """
    def __init__(self, graph = []):
        super().__init__(graph)

    def rand_create(self, num_nodes: int, num_edges: int):
        """ Randomly creates an NxN adjacency matrix (N =: num_nodes) with M (num_edges) edges.
        This will be a directed, unweighted graph that allows self-loop.
        """
        self.graph = [[0] * num_nodes for _ in range(num_nodes)]
        graph_coords = [(r, c) for r in range(num_nodes) for c in range(num_nodes)]
        edge_coords = sample(graph_coords, k=num_edges)
        for r, c in edge_coords:
            self.graph[r][c] = 1

    def plot_graph(self):
        """ Plots the previously created graph using `matplotlib` and the `networkx` frameworks.
        """
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
    graph = GridMatrix()
    graph.rand_create(200, has_path=True)
    graph.plot_graph()
