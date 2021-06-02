class Permutation:
    """Count the total number of permutations.
    nPr % mod.

    Args:
        max_value: Max size of list. The default is 500,050
        mod      : Modulo. The default is 10 ** 9 + 7.

    Landau notation: O(n)

    See:
    https://atcoder.jp/contests/abc133/submissions/6275589
    """

    def __init__(self, max_value=500050, mod=10 ** 9 + 7) -> None:
        self.max_value = max_value
        self.mod = mod
        self.fac = [1 for _ in range(self.max_value + 1)]
        self.inv = [1 for _ in range(self.max_value + 1)]

        for n in range(1, self.max_value + 1):
            self.fac[n] = (self.fac[n - 1] * n) % mod

        self.inv[self.max_value] = pow(self.fac[self.max_value], mod - 2, mod)

        for n in reversed(range(self.max_value)):
            self.inv[n] = (self.inv[n + 1] * (n + 1)) % mod

    def count_nPr(self, n, k) -> int:
        """Count the total number of permutations.
            nPr % mod.

        Args:
            n   : Elements. Int of number (greater than 1).
            k   : The number of k-th permutations. Int of number
                  (greater than 0).

        Returns:
            The total number of permutations.

        Landau notation: O(1)
        """

        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0

        return (self.fac[n] * self.inv[n - k]) % self.mod
