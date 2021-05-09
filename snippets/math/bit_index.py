from typing import List


def get_bit_index(number: int) -> List[int]:
    """Get bit indices from number.

    Args:
        number: A number (greater than 0).

    Returns:
        List of bit indices.

    Examples:
        number: 4 (`100` in 2 ary number), Returns: [3]
        number: 6 (`110` in 2 ary number), Returns: [2, 3]

    Landau notation: O(log number).
    """

    bit_index = list()
    index = 1

    while number:
        if number & 1:
            bit_index.append(index)

        index += 1
        number >>= 1

    return bit_index
