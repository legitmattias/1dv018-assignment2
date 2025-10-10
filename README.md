# Assignment 2 - Algorithms and Data Structures

Implementation of five data structures: linked list, deque, binary search tree, hashtable with separate chaining, and vehicle registry with custom hash function.

## Project Structure

```
assignment_2/
├── src/ads/              # Core implementations
│   ├── linked_list.py
│   ├── deque.py
│   ├── bst.py
│   ├── hashtable.py
│   └── vehicle.py
├── notebooks/            # Demonstration notebooks
│   ├── task1_linked_list_demo.ipynb
│   ├── task2_deque_demo.ipynb
│   ├── task3_bst_demo.ipynb
│   ├── task4_hashtable_demo.ipynb
│   └── task5_vehicle_registry_demo.ipynb
├── assignment2_report.md # Written report
├── activate.sh           # Environment activation script
├── lint.sh              # Linting script
├── environment.yml       # Conda environment specification
└── pyproject.toml       # Package configuration
```

## Setup

**Environment activation:**
```bash
source activate.sh
```

This script detects your conda installation, creates the `assignment2` environment from `environment.yml` if needed, and activates it.

**Install package in development mode:**
```bash
pip install -e .
```

This makes the `ads` package importable from notebooks.

## Running the Code

**View demonstrations:**
```bash
jupyter notebook
```

Open any of the `notebooks/task*.ipynb` files. Each notebook demonstrates the corresponding data structure with examples and analysis.

**Linting and formatting:**
```bash
./lint.sh
```

Runs `ruff check . --fix` and `ruff format .`

**Type checking:**
```bash
mypy src/
```

## Implementation Details

### Use of `yield` for Iterators

All iterators are implemented with Python's `yield` keyword rather than returning lists. This design choice provides:

1. **Memory efficiency**: Generators use O(1) space instead of O(n) for building complete lists
2. **Early termination**: Iteration can stop without computing remaining values
3. **Standard pattern**: `yield` is the standard Python approach for implementing iterators
4. **Recursive composition**: `yield from` enables clean recursive traversals in BST without building intermediate lists

**Example from BST in-order traversal:**
```python
def _inorder_helper(self, node):
    if node is not None:
        yield from self._inorder_helper(node.left)
        yield node.key
        yield from self._inorder_helper(node.right)
```

This pattern is used in:
- **LinkedList** (`linked_list.py`): Traverse from head to tail
- **Deque** (`deque.py`): Iterate from head to tail
- **BST** (`bst.py`): In-order, pre-order, and post-order traversals

### Other Technical Choices

**Python 3.12 generics**: Type variables defined with `[T]` syntax instead of `TypeVar`
```python
class LinkedList[T]:
    def __init__(self) -> None:
        self._head: LLNode[T] | None = None
```

**Recursive implementations**: BST operations (add, remove, contains) and hashtable chain operations use recursion

**Dataclasses**: Used for nodes and Vehicle class. Vehicle is `frozen=True` to be hashable

**Type hints**: All functions have complete type annotations for parameters and return values

## Notebooks

Each notebook demonstrates a specific task:

- **task1_linked_list_demo.ipynb**: Basic operations, comparison with ArrayList
- **task2_deque_demo.ipynb**: Operations, usage as stack and queue
- **task3_bst_demo.ipynb**: Operations, traversals, removeKthLargest, degenerate case
- **task4_hashtable_demo.ipynb**: Operations, collision handling, distribution analysis
- **task5_vehicle_registry_demo.ipynb**: Vehicle storage, hash function analysis, visualization

The notebooks generate plots and statistics for analysis. All use the implementations from `src/ads/`.

## Report

See `assignment2_report.md` for the written analysis answering the assignment questions:
1. Linked List vs ArrayList advantages/disadvantages
2. Hash function quality analysis for vehicle registry

## Code Quality

- Linted with Ruff (rules: E, F, W, I, UP, B, C, PL)
- Type-checked with mypy
- Formatted with Ruff (88 character line length, 4-space indent)
- All code passes checks without errors
