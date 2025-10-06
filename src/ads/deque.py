from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DLLNode[T]:
    """Node in a doubly linked list."""

    val: T
    nxt: DLLNode[T] | None = None
    prv: DLLNode[T] | None = None


class Deque[T]:
    """Double-ended queue implementation using doubly linked list."""

    def __init__(self) -> None:
        self._head: DLLNode[T] | None = None
        self._tail: DLLNode[T] | None = None
        self._count: int = 0

    def isEmpty(self) -> bool:
        """Check if deque is empty."""
        return self._head is None

    def size(self) -> int:
        """Return number of elements in deque."""
        return self._count

    def addFirst(self, item: T) -> None:
        """Add element at the beginning of the deque."""
        node = DLLNode(item, nxt=self._head)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._head.prv = node
            self._head = node
        self._count += 1

    def addLast(self, item: T) -> None:
        """Add element at the end of the deque."""
        node = DLLNode(item, prv=self._tail)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.nxt = node
            self._tail = node
        self._count += 1

    def removeFirst(self) -> T:
        """Remove and return first element. Raises IndexError if empty."""
        if self._head is None:
            raise IndexError("Cannot remove from empty deque")
        val = self._head.val
        self._head = self._head.nxt
        if self._head is None:
            self._tail = None
        else:
            self._head.prv = None
        self._count -= 1
        return val

    def removeLast(self) -> T:
        """Remove and return last element. Raises IndexError if empty."""
        if self._tail is None:
            raise IndexError("Cannot remove from empty deque")
        val = self._tail.val
        self._tail = self._tail.prv
        if self._tail is None:
            self._head = None
        else:
            self._tail.nxt = None
        self._count -= 1
        return val

    def __iter__(self):
        """Iterate over elements from head to tail."""
        current = self._head
        while current is not None:
            yield current.val
            current = current.nxt
