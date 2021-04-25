from typing import Tuple


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """Solve a * x + b * y = gcd(a, b).

    Extended Euclidean algorithm.

    Args:
        a: Int of number (greater than 0).
        b: Int of number (greater than or equal to 0).

    Returns:
        gcd(a, b): Greatest common divisor (gcd).
        x: Int of number.
        y: Int of number.

    Landau notation: O(gcd(a, b))

    See:
    https://qiita.com/drken/items/b97ff231e43bce50199a
    https://www.youtube.com/watch?v=hY2FicqnAcc
    """

    if b == 0:
        return (a, 1, 0)

    g, x, y = extgcd(b, a % b)

    return g, y, x - (a // b) * y
