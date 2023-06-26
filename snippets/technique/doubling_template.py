n, k = map(int, input().split())
digit = 30  #  k = 10 ** 9 < 2 ** 30
dp = [[0 for _ in range(n + 1)] for _ in range(digit)]

# Doubling
for i in range(n + 1):
    dp[0][i] = 0  # TODO: Update value.

for d in range(1, digit):
    for j in range(n + 1):
        dp[d][j] = dp[d - 1][dp[d - 1][j]]

# Find the result of the k-th operation.
i = 0
pos = 0  # TODO: Update value.

while k > 0:
    if k & 1:
        pos = dp[i][pos]

    i += 1
    k >>= 1
