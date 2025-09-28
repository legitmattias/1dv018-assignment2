from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLNode[T]:
    val: T
    nxt: LLNode[T] | None = None


class LLStack[T]:
    def __init__(self) -> None:
        self._head: LLNode[T] | None = None  # empty = None

    def empty(self) -> bool:
        return self._head is None

    def top(self) -> T | None:
        return None if self._head is None else self._head.val

    def push(self, v: T) -> None:
        self._head = LLNode(v, self._head)

    def pop(self) -> None:
        if self._head is not None:
            self._head = self._head.nxt
