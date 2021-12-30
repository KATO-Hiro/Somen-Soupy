# -*- coding: utf-8 -*-

from snippets.data_structure.two_dim_list import TwoDimList


class TestTwoDimList:
    def test_two_dim_list(self):
        h, w = 7, 10
        td = TwoDimList(h, w)

        for hi in range(h):
            for wi in range(w):
                assert td.read(hi, wi) == 0

        td.insert(0, 0, 10)
        assert td.read(0, 0) == 10

        td.plus(0, 0, 1)
        assert td.read(0, 0) == 11

        td.plus(0, 0, -1)
        assert td.read(0, 0) == 10

        td.insert(h - 1, w - 1, 100)
        assert td.read(h - 1, w - 1) == 100

        td.plus(h - 1, w - 1, 100)
        assert td.read(h - 1, w - 1) == 200
