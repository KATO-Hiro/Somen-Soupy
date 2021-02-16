# -*- coding: utf-8 -*-
'''Snippets for string.

Available functions:
- to_titlecase: Convert the character string to titlecase.
'''


def to_titlecase(s: str) -> str:
    '''For example:
        >>> 'Hello world'.title()
        'Hello World'

    Args:
        str: String excluding apostrophes in contractions and possessives
             form word boundaries.

    Returns:
        A titlecased version of the string where words start with an
        uppercase character and the remaining characters are lowercase.

    See:
        https://docs.python.org/3.6/library/stdtypes.html#str.title
    '''

    return s.title()
