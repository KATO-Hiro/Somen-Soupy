# -*- coding: utf-8 -*-

from typing import List
import pytest

from snippets.math.matrix import mul_matrix, mul_vector, op1, op2, op3, op4


class TestMatrix:

    @pytest.mark.parametrize(('vector', 'try_count', 'expected'), [
        ([1, 2, 1], 0, [1, 2, 1]),
        ([1, 2, 1], 1, [2, -1, 1]),
        ([1, 2, 1], 2, [4, -1, 1]),
        ([1, 2, 1], 3, [1, 4, 1]),
        ([1, 2, 1], 4, [1, 0, 1]),
    ])
    def test_mul_vector(self, vector: List[int], try_count: int, expected: List[int]) -> None:
        identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        matrices = [identity_matrix]

        # HACK: These code are room to improve.
        # rotate 90 degrees clockwise.
        prev_matrix = matrices[-1]
        cur_matrix = mul_matrix(op1(), prev_matrix)
        matrices.append(cur_matrix)

        # reverse with respect to straight line x.
        prev_matrix = matrices[-1]
        x_axis_base = 3
        cur_matrix = mul_matrix(op3(x_axis_base), prev_matrix)
        matrices.append(cur_matrix)

        # rotate 90 degrees counterclockwise.
        prev_matrix = matrices[-1]
        cur_matrix = mul_matrix(op2(), prev_matrix)
        matrices.append(cur_matrix)

        # reverse with respect to straight line y.
        prev_matrix = matrices[-1]
        y_axis_base = 2
        cur_matrix = mul_matrix(op4(y_axis_base), prev_matrix)
        matrices.append(cur_matrix)

        # vector = [1, 2, 1]  # xi, yi, const = 1
        actual = mul_vector(matrices[try_count], vector)
        assert actual == expected
