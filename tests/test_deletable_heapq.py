# -*- coding: utf-8 -*-


from snippets.data_structure.deletable_heapq import DeletableHeapq


class TestDeletableHeapq:
    def test_build(self):
        # Ascending-order
        hq = DeletableHeapq()
        array = [i for i in range(1, 6)]

        hq.build(array)
        assert hq.q == [1, 2, 3, 4, 5]

        # Descending-order
        hq = DeletableHeapq(descending_order=True)
        array = [i for i in range(1, 6)]

        hq.build(array)
        assert hq.q == [-5, -4, -3, -1, -2]

    def test_push(self):
        # Ascending-order
        hq = DeletableHeapq()

        for i in range(1, 6):
            hq.push(i)

        assert hq.q == [1, 2, 3, 4, 5]

        # Descending-order
        hq = DeletableHeapq(descending_order=True)

        for i in range(1, 6):
            hq.push(i)

        assert hq.q == [-5, -4, -2, -1, -3]

    def test_erase(self):
        # Ascending-order
        hq = DeletableHeapq()

        for i in range(1, 6):
            hq.push(i)

        hq.erase(3)
        assert hq.p == [3]

        # Descending-order
        hq = DeletableHeapq(descending_order=True)

        for i in range(1, 6):
            hq.push(i)

        hq.erase(3)
        assert hq.p == [-3]

    def test_pop(self):
        # Ascending-order
        hq = DeletableHeapq()

        for i in range(1, 6):
            hq.push(i)

        for i in range(1, 6):
            actual = hq.pop()
            assert actual == i

        # Descending-order
        hq = DeletableHeapq(descending_order=True)

        for i in range(1, 6):
            hq.push(i)

        for i in reversed(range(1, 6)):
            actual = hq.pop()
            assert actual == i

    def test_top(self):
        # Ascending-order
        hq = DeletableHeapq()

        for i in range(1, 6):
            hq.push(i)

        actual = hq.top()
        assert actual == 1

        actual = hq.top()
        assert actual == 1

        # Descending-order
        hq = DeletableHeapq(descending_order=True)

        for i in range(1, 6):
            hq.push(i)

        actual = hq.top()
        assert actual == 5

        actual = hq.top()
        assert actual == 5
