from learning.calc.op import Op, doop
from learning.stack.llstack import LLStack


def calc(ops: LLStack[Op], digs: LLStack[int]) -> int:
    """
    Empties `ops` by repeatedly applying the top operator to the top two
    digits on `digs`. Pushes each result back to `digs`. Returns the final result.

    Adds a few sanity checks for underflow.
    """
    while not ops.empty():
        op = ops.top()
        if op is None:
            raise ValueError("Operator stack empty when expecting an operator")
        ops.pop()

        d1 = digs.top()
        digs.pop() if d1 is not None else None
        d2 = digs.top()
        digs.pop() if d2 is not None else None
        if d1 is None or d2 is None:
            raise ValueError("Digit stack underflow")

        digs.push(doop(op, d2, d1))
    res = digs.top()
    if res is None:
        raise ValueError("No result on digit stack")
    digs.pop()
    if not digs.empty():
        raise ValueError("Extra values left on digit stack")
    return res
