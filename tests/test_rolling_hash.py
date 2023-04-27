# -*- coding: utf-8 -*-

from snippets.string.rolling_hash import RollingHash


class TestRollingHash:

    def test_rolling_hash(self):
        s1 = "abababab"
        t1 = "abab"
        rh1 = RollingHash(s1)
        rh2 = RollingHash(t1)

        assert rh1.get(0, 4) == rh2.get(0, 4)
        assert rh1.get(2, 4) == rh2.get(2, 4)
        assert rh1.get(0, 4) != rh2.get(1, 4)
        assert rh1.get(0, 5) != rh2.get(0, 4)

        s2 = "agccga"
        t2 = "cga"
        rh3 = RollingHash(s2)
        rh4 = RollingHash(t2)

        assert rh3.get(0, 3) != rh4.get(0, 3)
        assert rh3.get(3, 6) == rh4.get(0, 3)
