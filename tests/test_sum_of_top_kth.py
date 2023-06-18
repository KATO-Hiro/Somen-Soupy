# -*- coding: utf-8 -*-


from snippets.data_structure.sum_of_top_kth import SumOfTopKth


class TestSumOfTopKth:
    def test_sum_of_top_kth_by_descending_order(self) -> None:
        s = SumOfTopKth(k=5, ascending_order=False)

        for ai in [3, 1, 4, 1, 5, 9, 2, 6]:
            s.add(ai)

        actual = s.query()
        expected = 27
        assert actual == expected

        s.discard(4)
        s.add(3)
        actual = s.query()
        expected = 26
        assert actual == expected

        s.set_k(8)
        actual = s.query()
        expected = 30
        assert actual == expected

        s.discard(2)
        s.add(10)
        actual = s.query()
        expected = 38
        assert actual == expected

    def test_sum_of_top_kth_by_ascending_order(self) -> None:
        s = SumOfTopKth(k=5, ascending_order=True)

        for ai in [3, 1, 4, 1, 5, 9, 2, 6]:
            s.add(ai)

        actual = s.query()
        expected = 11
        assert actual == expected

        s.discard(4)
        s.add(5)
        actual = s.query()
        expected = 12
        assert actual == expected

        s.set_k(8)
        actual = s.query()
        expected = 32
        assert actual == expected

        s.discard(6)
        s.add(2)
        actual = s.query()
        expected = 28
        assert actual == expected
