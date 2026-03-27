import numpy as np
import networkx as nx

class BratteliDiagram:
	def __init__(self):
	        """
	        Initializes the diagram starting with C (Level 0).
	        C is represented as a single block of dimension 1.
	        """
	        self.graph = nx.DiGraph()
	        self.levels = [[1]]

	        # Add the Level 0 vertex to the graph. 
	        # Node name is the tuple (level, index) -> (0, 0)
	        self.graph.add_node((0, 0), dimension=1)

	def add_level(self, multiplicity_matrix):
	        """
	        Adds the next level of the C*-algebra using a multiplicity matrix.
	        The matrix M describes the connecting *-homomorphism.
	        """
	        M = np.array(multiplicity_matrix)
	        
	        current_level_idx = len(self.levels) - 1
	        current_dims = np.array(self.levels[-1])
	        
	        # Calculate the dimensions of the matrix blocks at the new level
	        # by multiplying the multiplicity matrix by the current dimension vector.
	        next_dims = current_dims @ M
	        self.levels.append(next_dims.tolist())
	        
	        next_level_idx = current_level_idx + 1
	        
	        # Add the new nodes and the connecting edges
	        for j, dim in enumerate(next_dims):
	            self.graph.add_node((next_level_idx, j), dimension=int(dim))
	            
	            for i, _ in enumerate(current_dims):
	                edges = M[i,j]
	                if edges > 0:
	                    # Weight represents the number of edges (partial multiplicity)
	                    self.graph.add_edge((current_level_idx, i), (next_level_idx, j), weight=int(edges))

# Initialize with C (dimension 1)
car_algebra = BratteliDiagram()

# Add Level 1: C embeds into M_2(C) with multiplicity 2
car_algebra.add_level([[2]])

# Add Level 2: M_2(C) embeds into M_4(C) with multiplicity 2
car_algebra.add_level([[2]])

# Print the resulting block dimensions at each level
print("CAR Algebra block dimensions by level:")
for level_idx, dims in enumerate(car_algebra.levels):
    print(f"Level {level_idx}: {dims}")

print("\nGraph Nodes (Vertex, Attributes):")
# data=True forces NetworkX to reveal the hidden dimension dictionary
for node in car_algebra.graph.nodes(data=True):
    print(node)

print("\nGraph Edges (Source, Target, Attributes):")
# data=True reveals the edge weight (partial multiplicity)
for edge in car_algebra.graph.edges(data=True):
    print(edge)
