from enum import IntEnum


class Op(IntEnum):
    ADD = 1
    DIV = 2
    MUL = 3
    SUB = 4


def doop(op: Op, d1: int, d2: int) -> int:
    if op is Op.ADD:
        return d1 + d2
    if op is Op.DIV:
        return d1 // d2
    if op is Op.MUL:
        return d1 * d2
    if op is Op.SUB:
        return d1 - d2
    raise ValueError("Unknown op")
