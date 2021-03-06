# -*- coding: utf-8 -*-
import pytest

from snippets.string.string import to_titlecase


class TestString:

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
