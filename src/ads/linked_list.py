from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLNode[T]:
    """Node in a singly linked list."""

    val: T
    nxt: LLNode[T] | None = None


class LinkedList[T]:
    """Simple singly linked list implementation."""

    def __init__(self) -> None:
        self._head: LLNode[T] | None = None

    def empty(self) -> bool:
        """Check if list is empty."""
        return self._head is None

    def count(self) -> int:
        """Return number of elements in list."""
        cnt = 0
        current = self._head
        while current is not None:
            cnt += 1
            current = current.nxt
        return cnt

    def append(self, data: T) -> None:
        """Add element at the end of the list."""
        if self._head is None:
            self._head = LLNode(data)
        else:
            current = self._head
            while current.nxt is not None:
                current = current.nxt
            current.nxt = LLNode(data)

    def delete(self, data: T) -> None:
        """Remove first occurrence of data. Raises ValueError if not found."""
        if self._head is None:
            raise ValueError(f"Cannot delete {data} from empty list")

        # Special case: removing head
        if self._head.val == data:
            self._head = self._head.nxt
            return

        # Search for the node to delete
        current = self._head
        while current.nxt is not None:
            if current.nxt.val == data:
                current.nxt = current.nxt.nxt
                return
            current = current.nxt

        raise ValueError(f"Value {data} not found in list")

    def __len__(self) -> int:
        """Return number of elements in list."""
        return self.count()

    def __iter__(self):
        """Iterate over elements in the list."""
        current = self._head
        while current is not None:
            yield current.val
            current = current.nxt
