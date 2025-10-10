from __future__ import annotations

from ads.linked_list import LLNode


class HashTableSC[K, V]:
    """Hashtable using separate chaining for collision resolution.

    Each bucket contains a linked list of (key, value) pairs that hash to
    the same position.
    """

    def __init__(self, m: int = 31) -> None:
        """Initialize hashtable with m buckets.

        Args:
            m: Table size (should be prime for better distribution)
        """
        self.sz = m
        self.table: list[LLNode[tuple[K, V]] | None] = [None] * self.sz

    def put(self, key: K, value: V) -> None:
        """Insert or update key-value pair.

        Args:
            key: Key to insert/update
            value: Value to associate with key
        """
        hv = hash(key) % self.sz
        self.table[hv] = self._put_chain(self.table[hv], key, value)

    def _put_chain(
        self, node: LLNode[tuple[K, V]] | None, key: K, value: V
    ) -> LLNode[tuple[K, V]]:
        """Recursively insert/update in chain.

        Args:
            node: Current node in chain
            key: Key to insert/update
            value: Value to associate

        Returns:
            Updated chain head
        """
        if node is None:
            return LLNode((key, value))

        # Update if key exists
        if node.val[0] == key:
            node.val = (key, value)
            return node

        # Recurse to end of chain
        node.nxt = self._put_chain(node.nxt, key, value)
        return node

    def get(self, key: K) -> V | None:
        """Retrieve value by key.

        Args:
            key: Key to look up

        Returns:
            Value if found, None otherwise
        """
        hv = hash(key) % self.sz
        return self._get_chain(self.table[hv], key)

    def _get_chain(self, node: LLNode[tuple[K, V]] | None, key: K) -> V | None:
        """Recursively search chain for key.

        Args:
            node: Current node in chain
            key: Key to find

        Returns:
            Value if found, None otherwise
        """
        if node is None:
            return None
        if node.val[0] == key:
            return node.val[1]
        return self._get_chain(node.nxt, key)

    def contains(self, key: K) -> bool:
        """Check if key exists in table.

        Args:
            key: Key to check

        Returns:
            True if key exists, False otherwise
        """
        hv = hash(key) % self.sz
        return self._contains_chain(self.table[hv], key)

    def _contains_chain(self, node: LLNode[tuple[K, V]] | None, key: K) -> bool:
        """Recursively search chain for key.

        Args:
            node: Current node in chain
            key: Key to find

        Returns:
            True if key found, False otherwise
        """
        if node is None:
            return False
        if node.val[0] == key:
            return True
        return self._contains_chain(node.nxt, key)

    def remove(self, key: K) -> bool:
        """Remove key-value pair from table.

        Args:
            key: Key to remove

        Returns:
            True if key was removed, False if not found
        """
        hv = hash(key) % self.sz
        new_head, removed = self._remove_chain(self.table[hv], key)
        self.table[hv] = new_head
        return removed

    def _remove_chain(
        self, node: LLNode[tuple[K, V]] | None, key: K
    ) -> tuple[LLNode[tuple[K, V]] | None, bool]:
        """Recursively remove key from chain.

        Args:
            node: Current node in chain
            key: Key to remove

        Returns:
            Tuple of (updated chain head, success flag)
        """
        if node is None:
            return (None, False)

        # Found key - remove this node
        if node.val[0] == key:
            return (node.nxt, True)

        # Recurse and update link
        new_next, removed = self._remove_chain(node.nxt, key)
        node.nxt = new_next
        return (node, removed)

    def is_empty(self) -> bool:
        """Check if table is empty.

        Returns:
            True if no entries, False otherwise
        """
        return len(self) == 0

    def keys(self) -> list[K]:
        """Get all keys in table.

        Returns:
            List of all keys
        """
        result = []
        for bucket in self.table:
            current = bucket
            while current is not None:
                result.append(current.val[0])
                current = current.nxt
        return result

    def values(self) -> list[V]:
        """Get all values in table.

        Returns:
            List of all values
        """
        result = []
        for bucket in self.table:
            current = bucket
            while current is not None:
                result.append(current.val[1])
                current = current.nxt
        return result

    def __len__(self) -> int:
        """Return total number of entries.

        Returns:
            Number of key-value pairs
        """
        total = 0
        for bucket in self.table:
            total += self._len_chain(bucket)
        return total

    def _len_chain(self, node: LLNode[tuple[K, V]] | None) -> int:
        """Count nodes in chain.

        Args:
            node: Chain head

        Returns:
            Number of nodes in chain
        """
        count = 0
        current = node
        while current is not None:
            count += 1
            current = current.nxt
        return count
