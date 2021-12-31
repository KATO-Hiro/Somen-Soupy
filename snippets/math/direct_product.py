# -*- coding: utf-8 -*-

# n = int(input())
# m = int(input())

# Sample Input
n, m = 10, 2

# Examples:
#     n, m = 10, 2
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
#     ...
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def direct_product(arr):
    '''Template for direct product.

    Args:
        arr: List of numbers.

    Landau notation: O(m ** n)

    See:
    https://drken1215.hatenablog.com/entry/2020/05/04/190252
    '''

    if len(arr) == n:
        # if cond:
        #     # do something
        #     return
        return # Return some value if needs
    
    # count = 0 # Initialize count
    
    for i in range(m):
        # backtracking
        arr.append(i)
        direct_product(arr)
        # count += direct_product(arr) # Update count
        arr.pop() # Important
    
    # return count # Important

direct_product([])


# Examples:
# Input:
#  arr = [[1, 2, 3], [4, 5]]
# 
# Output:
# [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
def get_direct_product(arr):
    from itertools import product

    return list(product(*arr))

arr = [[1, 2, 3], [4, 5]]
print(get_direct_product(arr))
