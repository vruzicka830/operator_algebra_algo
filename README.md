# Operator Algebra Algorithms

Python implementation of core data structures and algorithms from the theory of operator algebras, focusing on finite-dimensional C\*-algebras and their inductive limits via Bratteli diagrams.

## Background

A **finite-dimensional C\*-algebra** is isomorphic to a direct sum of full matrix algebras:

$$A \cong M_{n_1}(\mathbb{C}) \oplus M_{n_2}(\mathbb{C}) \oplus \cdots \oplus M_{n_k}(\mathbb{C})$$

and is completely determined by its list of block dimensions $(n_1, n_2, \ldots, n_k)$.

A **Bratteli diagram** encodes a sequence of C\*-algebra embeddings $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$. Each embedding is described by a *multiplicity matrix* $M$, whose $(i,j)$ entry counts how many times the $i$-th summand of $A_n$ maps into the $j$-th summand of $A_{n+1}$. The inductive limit of this sequence is a (generally infinite-dimensional) C\*-algebra — for example, the **CAR algebra** (Canonical Anticommutation Relations), which arises in quantum mechanics.

## Modules

**`finite_dim_C_algebra.py`** — `FiniteDimCAlgebra`

Represents a finite-dimensional C\*-algebra by its block dimensions. Computes the vector space dimension $\sum n_i^2$ and generates random elements as block-diagonal complex matrices.

**`direct_sum.py`** — `direct_sum(A, B)`

Constructs the matrix direct sum $A \oplus B$ as a block-diagonal numpy array.

**`construct_Bratteli.py`** — `BratteliDiagram`

Builds a Bratteli diagram incrementally using NetworkX. Each call to `add_level(M)` appends a new level of the diagram using a multiplicity matrix, computing new block dimensions via `next_dims = current_dims @ M` and recording the graph structure of the embedding.

## Example

```python
from construct_Bratteli import BratteliDiagram

# Construct the first few levels of the CAR algebra
diagram = BratteliDiagram()       # Level 0: C
diagram.add_level([[2]])           # Level 1: M_2(C)
diagram.add_level([[2]])           # Level 2: M_4(C)

for level_idx, dims in enumerate(diagram.levels):
    print(f"Level {level_idx}: {dims}")
# Level 0: [1]
# Level 1: [2]
# Level 2: [4]
```

## Setup

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Dependencies

- [NumPy](https://numpy.org/) — matrix construction and linear algebra
- [NetworkX](https://networkx.org/) — directed graph representation of Bratteli diagrams
- [Matplotlib](https://matplotlib.org/) — diagram visualization (in progress)
