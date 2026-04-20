import numpy as np

class FiniteDimCAlgebra:
    """
	represents a finite-dimensional C*-algebra by matrix block sizes.

    Attributes:
        block_dimensions: List of positive integers specifying the dimension of each block
        num_blocks: Number of blocks in the algebra
    """

    def __init__(self, block_dimensions):
        """
        Initialize a finite-dimensional C*-algebra with specified block dimensions.
        """
        # Validate input type
        if not isinstance(block_dimensions, list):
            raise TypeError("Block dimensions must be a list.")

        # Validate each dimension
        for dimension in block_dimensions:
            if not isinstance(dimension, int):
                raise TypeError("Individual dimensions must be positive integers.")
            if dimension <= 0:
                raise ValueError("Individual dimensions must be positive.")

        self.block_dimensions = block_dimensions
        self.num_blocks = len(block_dimensions)

    def dimension(self):
        """
        Calculate the dimension of the C*-algebra (as vector space))
        """
        total_dimension = 0
        for block_dim in self.block_dimensions:
            total_dimension += block_dim ** 2
        return total_dimension

    def random_element(self):
        """
        Generate a random element of the C*-algebra as a block diagonal matrix.
        Returns:
            A complex numpy array of shape (n, n) where n is the sum of all block dimensions.
        """
        # Calculate total size of the matrix
        total_size = sum(self.block_dimensions)

        # Create empty block diagonal matrix
        element = np.zeros((total_size, total_size), dtype=complex)

        # Fill each block with random complex values
        current_index = 0
        for block_dim in self.block_dimensions:
            # Generate random real and imaginary parts
            real_part = np.random.rand(block_dim, block_dim)
            imaginary_part = np.random.rand(block_dim, block_dim)

            # Combine into complex block
            block = real_part + 1j * imaginary_part

            # Place block in the correct position on the diagonal
            element[current_index:current_index + block_dim,
                    current_index:current_index + block_dim] = block

            current_index += block_dim

        return element

'''Example:
algebra = FiniteDimCAlgebra([2,3,4])
print(algebra.num_blocks,algebra.dimension())
element = algebra.random_element()
print(element, element.shape)
'''
