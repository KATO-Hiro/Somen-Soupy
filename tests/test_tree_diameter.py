# import pytest

import pytest

from snippets.graph.tree_diameter import TreeDiameter


class TestTreeDiameter:
    @pytest.mark.parametrize(
        ("n", "inputs", "expected"),
        [
            (4, [(1, 2, 2), (1, 3, 3), (1, 4, 4)], 7),
            (
                10,
                [
                    (10, 9, 1000000000),
                    (9, 8, 1000000000),
                    (8, 7, 1000000000),
                    (7, 6, 1000000000),
                    (6, 5, 1000000000),
                    (5, 4, 1000000000),
                    (4, 3, 1000000000),
                    (3, 2, 1000000000),
                    (2, 1, 1000000000),
                ],
                9000000000,
            ),
            (
                11,
                [
                    (1, 6, 16),
                    (10, 5, 11),
                    (4, 11, 8),
                    (7, 3, 18),
                    (4, 5, 12),
                    (11, 1, 20),
                    (3, 8, 13),
                    (2, 6, 12),
                    (9, 11, 10),
                    (7, 11, 15),
                ],
                94,
            ),
            (
                24,
                [
                    (8, 12, 26),
                    (11, 6, 21),
                    (2, 16, 13),
                    (14, 1, 1),
                    (19, 16, 8),
                    (16, 7, 14),
                    (16, 22, 29),
                    (1, 5, 13),
                    (17, 1, 17),
                    (15, 8, 22),
                    (10, 3, 23),
                    (17, 9, 7),
                    (19, 4, 25),
                    (21, 18, 15),
                    (3, 4, 4),
                    (11, 21, 5),
                    (2, 8, 15),
                    (24, 23, 8),
                    (9, 21, 16),
                    (13, 1, 3),
                    (17, 23, 5),
                    (16, 20, 23),
                    (20, 17, 25),
                ],
                157,
            ),
        ],
    )
    def test_calc(
        self, n: int, inputs: list[tuple[int, int, int]], expected: int
    ) -> None:
        graph = [[] for _ in range(n)]

        # 1-indexed to 0-indexed
        for ai, bi, ci in inputs:
            ai -= 1
            bi -= 1

            graph[ai].append((ci, bi))
            graph[bi].append((ci, ai))

        tree_diameter = TreeDiameter(vertex_count=n, graph=graph)
        dist, _, _ = tree_diameter.calc(source=0)

        assert dist == expected
