# -*- coding: utf-8 -*-


import pytest

from snippets.string.string import to_titlecase
from snippets.string.string import get_offset


class TestString:

    @pytest.mark.parametrize(('alphabet', 'base_alphabet', 'expected'), [
        ('A', '', 0),
        ('B', '', 1),
        ('Y', '', 24),
        ('Z', '', 25),
        ('A', 'A', 0),
        ('Y', 'A', 24),
        ('Z', 'A', 25),
        ('a', 'a', 0),
        ('b', 'a', 1),
        ('y', 'a', 24),
        ('z', 'a', 25),
    ])
    def test_get_offset(self, alphabet: str, base_alphabet: str, expected: int):
        if base_alphabet == '':
            actual = get_offset(alphabet)
        else:
            actual = get_offset(alphabet, base_alphabet)

        assert actual == expected

    @pytest.mark.parametrize(('string', 'expected'), [
        ('hello world.', 'Hello World.'),
        ('Hello world.', 'Hello World.'),
        ('hello World.', 'Hello World.'),
        ('Hello World.', 'Hello World.'),
        ('hEllo world.', 'Hello World.'),
    ])
    def test_to_titlecase(self, string, expected):
        actual = to_titlecase(string)
        assert actual == expected
