# -*- coding: utf-8 -*-


import pytest

from snippets.string.string import add_offset_to_alphabet
from snippets.string.string import get_offset
from snippets.string.string import to_titlecase


class TestString:

    @pytest.mark.parametrize(('offset', 'base_alphabet', 'expected'), [
        (0, '', 'A'),
        (1, '', 'B'),
        (24, '', 'Y'),
        (25, '', 'Z'),
        (0, 'a', 'a'),
        (1, 'a', 'b'),
        (24, 'a', 'y'),
        (25, 'a', 'z'),
    ])
    def test_add_offset_to_alphabet(self, offset: int, base_alphabet: str, expected: str):
        if base_alphabet == '':
            actual = add_offset_to_alphabet(offset)
        else:
            actual = add_offset_to_alphabet(offset, base_alphabet)

        assert actual == expected

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
