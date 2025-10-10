from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BSTNode[T]:
    """Node in a binary search tree."""

    key: T
    left: BSTNode[T] | None = None
    right: BSTNode[T] | None = None


class BST[T]:
    """Binary search tree implementation."""

    def __init__(self) -> None:
        self._root: BSTNode[T] | None = None

    def height(self) -> int:
        """Return height of tree. Empty tree has height 0."""
        return self._height_helper(self._root)

    def _height_helper(self, node: BSTNode[T] | None) -> int:
        if node is None:
            return 0
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))

    def size(self) -> int:
        """Return number of nodes in tree."""
        return self._size_helper(self._root)

    def _size_helper(self, node: BSTNode[T] | None) -> int:
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)

    def add(self, key: T) -> None:
        """Add key to tree."""
        self._root = self._add_helper(self._root, key)

    def _add_helper(self, node: BSTNode[T] | None, key: T) -> BSTNode[T]:
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._add_helper(node.left, key)
        elif key > node.key:
            node.right = self._add_helper(node.right, key)
        return node

    def contains(self, key: T) -> bool:
        """Check if key exists in tree."""
        return self._contains_helper(self._root, key)

    def _contains_helper(self, node: BSTNode[T] | None, key: T) -> bool:
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._contains_helper(node.left, key)
        return self._contains_helper(node.right, key)

    def remove(self, key: T) -> None:
        """Remove key from tree. Raises ValueError if not found."""
        self._root = self._remove_helper(self._root, key)

    def _remove_helper(self, node: BSTNode[T] | None, key: T) -> BSTNode[T] | None:
        if node is None:
            raise ValueError(f"Key {key} not found in tree")
        if key < node.key:
            node.left = self._remove_helper(node.left, key)
        elif key > node.key:
            node.right = self._remove_helper(node.right, key)
        else:
            # Found node to remove
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Two children: replace with smallest in right subtree
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._remove_helper(node.right, min_node.key)
        return node

    def _find_min(self, node: BSTNode[T]) -> BSTNode[T]:
        while node.left is not None:
            node = node.left
        return node

    def inorder_iter(self):
        """Iterate in-order (left-root-right). Produces sorted sequence."""
        yield from self._inorder_helper(self._root)

    def _inorder_helper(self, node: BSTNode[T] | None):
        if node is not None:
            yield from self._inorder_helper(node.left)
            yield node.key
            yield from self._inorder_helper(node.right)

    def preorder_iter(self):
        """Iterate pre-order (root-left-right)."""
        yield from self._preorder_helper(self._root)

    def _preorder_helper(self, node: BSTNode[T] | None):
        if node is not None:
            yield node.key
            yield from self._preorder_helper(node.left)
            yield from self._preorder_helper(node.right)

    def postorder_iter(self):
        """Iterate post-order (left-right-root)."""
        yield from self._postorder_helper(self._root)

    def _postorder_helper(self, node: BSTNode[T] | None):
        if node is not None:
            yield from self._postorder_helper(node.left)
            yield from self._postorder_helper(node.right)
            yield node.key

    def removeKthLargest(self, k: int) -> None:
        """Remove k-th largest element. Raises ValueError if k invalid."""
        if k < 1 or k > self.size():
            raise ValueError(f"Invalid k={k} for tree of size {self.size()}")
        sorted_keys = list(self.inorder_iter())
        key_to_remove = sorted_keys[-(k)]
        self.remove(key_to_remove)
